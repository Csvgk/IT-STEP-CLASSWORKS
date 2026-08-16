class Player:

    def __init__(self,name):
        self.name = name
        self.login = 'qwerty'

    def get_name(self):
        return self.name

    def set_name(self,new_name):
        self.name = new_name

new_player1 = Player("Nick")
print(new_player1.name)

new_player1.name = 'error'
print(new_player1.name)

#створити клас студент, і додати атрибути імя, вік, сер.оцінка
print()

class Student:

    def __init__(self,name,age,avg):
        self.name = name
        self.__age = age
        self.__id = 123

    def show_info(self):
        return f"Name: {self.name}; Age: {self.__age} ID: {self.__id}"

    def get_age(self):
        return self.__age

    def set_age(self,age):
        if age > 0:
            self.__age = age

    def __get_id(self):
        return self.__id

stud1 = Student('Nick',21,10)
print(stud1.name)

stud1.set_age(52)
print(stud1.show_info())