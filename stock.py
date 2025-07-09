from datetime import datetime
from medicine import Medicine

class MedicineStock:
    def __init__(self, medicine: Medicine, batch_info: str, batch_number: str ,quantity: int, expiry_date: str):
        self.__medicine = medicine
        self.__batch_info = batch_info
        self.__quantity = quantity
        self.__expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d')
        self.__batch_number = batch_number

    def get_medicine(self):
        return self.__medicine

    def get_batch_info(self):
        return self.__batch_info

    def get_quantity(self):
        return self.__quantity

    def get_expiry_date(self):
        return self.__expiry_date
    
    def get_batch_number(self):
        return self.__batch_number
    
    def update_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.__quantity = quantity

    def is_expired(self):
        return datetime.today().date() > self.__expiry_date.date()

    def display_info(self):
        print("Medicine Stock Information:")
        print(f"Medicine: {self.get_medicine().get_name()}")
        print(f"Batch Number: {self.get_batch_number()}")
        print(f"Quantity: {self.get_quantity()}")
        print(f"Expiry Date: {self.get_expiry_date().strftime('%Y-%m-%d')}")