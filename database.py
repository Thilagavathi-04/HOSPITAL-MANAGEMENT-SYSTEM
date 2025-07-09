import sqlite3

conn = sqlite3.connect("hospital.db")

cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    gender TEXT NOT NULL,
                    diagnosis TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
                )   
                ''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS medicine (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    description TEXT NOT NULL
                )
                ''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS medicine_stock (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    medicine_id INTEGER NOT NULL,
                    batch_info TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    expiry_date DATE NOT NULL,
                    batch_number TEXT NOT NULL,
                    FOREIGN KEY (medicine_id) REFERENCES medicine(id)
                )
                ''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS prescriptions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    patient_id INTEGER NOT NULL,
                    medicine_id INTEGER NOT NULL,
                    dosage TEXT NOT NULL,
                    start_date DATE NOT NULL,
                    end_date DATE NOT NULL,
                    FOREIGN KEY (patient_id) REFERENCES patients(id),
                    FOREIGN KEY (medicine_id) REFERENCES medicine(id)
                )
                ''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    role TEXT NOT NULL CHECK(role IN ('admin', 'staff', 'doctor'))
                )
                ''')

conn.commit()   