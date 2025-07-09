from database import conn , cursor
from user import User
from patient import Patient
from medicine import Medicine
from stock import MedicineStock 
from prescriptions import Prescription

current_user = {"Name": None, "Role": None}

# REGISTRATION FUNCTION
def register():
    print("Register a new user")
    username = input("Enter username: ")        
    password = input("Enter password: ")
    role = input("Enter role (admin, staff, doctor): ").lower()

    try:
        user = User(username, password, role)
        user.save_to_db(cursor)
        conn.commit()
        print("User registered successfully.")
    except:
        print("Error: User registration failed. Please try again.")

# LOGIN FUNCTION        
def login():
    print("Login")
    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()        

    if user:
        stored_password = user[2]    
        role = user[3]

        import hashlib
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        if hashed_password == stored_password:
            current_user["Name"] = username
            current_user["Role"] = role
            print(f"Login successful. Welcome {username}!")
            return True
        else:
            print("Error: Incorrect password.")
            return False
    else:
        print("Error: User not found.")
        return False   
    
# ADMIN FEATURES    
def add_medicine():
    print("Add Medicine")
    name= input("Enter medicine name: ")
    category = input("Enter medicine category (Tablet/Syrup/Injection): ")  
    description = input("Enter medicine description: ")
    medicine = Medicine(name, category, description)
    medicine.display_info() 

    cursor.execute('''
        INSERT INTO medicine (name, category, description)
        VALUES (?, ?, ?)
    ''', (medicine.get_name(), medicine.get_category(), medicine.get_description()))    
    conn.commit()
    print("Medicine added successfully")

def add_stock():
    print("Add Medicine Stock")
    name = input("Enter medicine name: ")
    category = input("Enter medicine category: ")
    description = input("Enter medicine description: ")
    batch_info = input("Enter batch information: ")
    batch_number = input("Enter batch number: ")
    quantity = int(input("Enter quantity: "))
    expiry_date = input("Enter expiry date (YYYY-MM-DD): ")

    cursor.execute('SELECT id FROM medicine WHERE name = ?', (name,))
    medicine_id = cursor.fetchone()

    if medicine_id:
        medicine_id = medicine_id[0]
    else:    
        medicine = Medicine(name, category, description)

        cursor.execute('''
        INSERT INTO medicine (name, category, description)
        VALUES (?, ?, ?)
        ''', (name, category, description))
    conn.commit()
    medicine_id = cursor.lastrowid

    stock = MedicineStock(Medicine(name, category, description), batch_info,batch_number, quantity, expiry_date)
    stock.display_info()
  
    cursor.execute('''
        INSERT INTO medicine_stock (medicine_id, batch_info, quantity, expiry_date, batch_number)
        VALUES (?, ?, ?, ?, ?)
    ''', (medicine_id, stock.get_batch_info(), stock.get_quantity(), stock.get_expiry_date().strftime('%Y-%m-%d'), batch_number))
    conn.commit()   
    print("Medicine stock added successfully")

# DOCTOR FEATURES   
def add_patient():
    print("Add Patient")
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender: ")
    diagnosis = input("Enter patient diagnosis: ")
    patient= Patient(name,age,gender,diagnosis)
    patient.display_info()

    cursor.execute('''
        INSERT INTO patients (name,age,gender,diagnosis,created_at)
        VALUES (?, ?, ?, ?,?)
    ''', (patient.get_name(), patient.get_age(), patient.get_gender(), patient.get_diagnosis(), patient.get_created_at().strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()
    print("Patient added successfully")

def add_prescription():
    print("Add Prescription")
    patient_name = input("Enter patient name: ")
    medicine_name = input("Enter medicine name: ")  
    dosage = input("Enter dosage: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    cursor.execute('SELECT id FROM patients WHERE name = ?', (patient_name,))
    patient_data = cursor.fetchone()

    cursor.execute('SELECT id, category, description FROM medicine WHERE name = ?', (medicine_name,))
    medicine_data = cursor.fetchone()

    if not patient_data or not medicine_data:
        print("Error: Patient or Medicine not found.")
        return

    patient = Patient(patient_name, 0, "", "") 
    medicine = Medicine(medicine_name, medicine_data[1], medicine_data[2])

    prescription = Prescription(patient, medicine, dosage, start_date, end_date)
    prescription.display_info()

    cursor.execute('''
        INSERT INTO prescriptions (patient_id, medicine_id, dosage, start_date, end_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (patient_data[0], medicine_data[0], dosage, start_date, end_date))

    conn.commit()
    print("Prescription added successfully")

# STAFF FEATURES
def view_stock():
    print("View Medicine Stock")
    cursor.execute('SELECT * FROM medicine_stock')
    stocks = cursor.fetchall()

    if stocks:
        for stock in stocks:
            print(f"Medicine ID: {stock[1]}, Batch Info: {stock[2]}, Quantity: {stock[3]}, Expiry Date: {stock[4]}, Batch Number: {stock[5]}")
    else:
        print("No stock available")

# ROLE BASED FUNCTIONALITY  
def show_menu():
    role = current_user["Role"]
    while True:
        print("\n MENU:")
        if role == "admin":  
                print("1. Add Medicine\n2. Add Stock\n3. Logout")
                opt = input("Select: ")
                if opt == "1": 
                    add_medicine()
                elif opt == "2":
                    add_stock() 
                elif opt == "3":
                    break
                else:
                    print("Invalid option. Please try again")      

        elif role == "doctor":
            print("1. Add Patient\n2. Add Prescription\n3. Logout")
            opt = input("Select: ")
            if opt == "1":
                add_patient()
            elif opt == "2":
                add_prescription()
            elif opt == "3":
                break
            else:
                print("Invalid option. Please try again")

        elif role == "staff":
            print("1. View Stock\n2. Logout")
            opt = input("Select: ")
            if opt == "1":
                view_stock()
            elif opt == "2":
                break
            else:
                print("Invalid option. Please try again")

# MAIN ENTRY POINT
def main():
    print("Welcome to Hospital Management System")

    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            register()
        elif choice == "2":
            if login():
                show_menu()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid input. Please try again")

    conn.close()    

if __name__ == "__main__":
    main()                                   