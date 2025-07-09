import hashlib

class User:
    def __init__(self, username, password,role):
        self.__username = username
        self.__password = self.__hash_password(password)
        self.__role = role.lower() 

        if self.__role not in ['admin', 'staff', 'doctor']:
            raise ValueError("Role must be one of 'admin', 'staff', or 'doctor'")

    def __hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password
    
    def verify_password(self, password):
        return self.__hash_password(password) == self.__password
    
    def save_to_db(self, cursor):
        cursor.execute('''
            INSERT INTO users (username, password, role)
            VALUES (?, ?, ?)
        ''', (self.__username, self.__password, self.__role))

    def display_info(self):
        print("User Information:")
        print(f"Username: {self.get_username()}")
        print(f"Password Hash: {self.get_password()}")