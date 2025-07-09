from abc import ABC, abstractmethod 
from datetime import datetime

class Displayable(ABC):
    @abstractmethod
    def display_info(self):
        pass

class Person:
    def __init__(self,name,age,gender):
        self.__name=name
        self.__age=age
        self.__gender=gender

    def get_name(self):
        return self.__name

    def get_age(self):              
        return self.__age

    def get_gender(self):
        return self.__gender

class Patient(Person, Displayable):
    def __init__(self,name,age,gender,diagnosis):
        super().__init__(name,age,gender)
        self.__diagnosis = diagnosis
        self.__created_at = datetime.now()

    def get_diagnosis(self):
        return self.__diagnosis 
    
    def get_created_at(self):
        return self.__created_at

    def display_info(self):
        print("Patient Information:")
        print(f"Patient Name: {self.get_name()}")
        print(f"Age:          {self.get_age()}")
        print(f"Gender:       {self.get_gender()}")
        print(f"Diagnosis:    {self.__diagnosis}")
        print(f"Created At:   {self.__created_at}")   

    