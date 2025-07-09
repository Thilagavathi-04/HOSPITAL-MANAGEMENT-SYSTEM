from abc import ABC, abstractmethod

class Displayable(ABC):
    @abstractmethod
    def display_info(self):
        pass    

class Medicine(Displayable):
    def __init__(self, name, category, description):
        self.__name = name
        self.__category = category
        self.__description = description

    def get_name(self):
        return self.__name

    def get_category(self):
        return self.__category

    def get_description(self):
        return self.__description

    def display_info(self):
        print("Medicine Information:")
        print(f"Medicine Name: {self.get_name()}")
        print(f"Category:      {self.get_category()}")
        print(f"Description:   {self.get_description()}")    