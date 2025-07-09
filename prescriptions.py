from patient import Patient
from medicine import Medicine
from datetime import datetime

class Prescription:
    def __init__(self, patient: Patient, medicine: Medicine, dosage: str, start_date: str, end_date: str):
        self.__patient = patient
        self.__medicine = medicine
        self.__dosage = dosage
        self.__start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        self.__end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

    def get_patient(self):
        return self.__patient

    def get_medicine(self):
        return self.__medicine

    def get_dosage(self):
        return self.__dosage

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def display_info(self):
        print("Prescription Information:")
        print(f"Patient:   {self.get_patient().get_name()}")
        print(f"Medicine:  {self.get_medicine().get_name()}")
        print(f"Dosage:    {self.get_dosage()}")
        print(f"Start Date:{self.get_start_date().strftime('%Y-%m-%d')}")
        print(f"End Date:  {self.get_end_date().strftime('%Y-%m-%d')}")