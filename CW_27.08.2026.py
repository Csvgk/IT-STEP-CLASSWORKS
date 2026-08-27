from abc import ABC, abstractmethod


class AbstractBasePlayer(ABC):
    def __init__(self, name, rasa):
        self.name = name
        self.rasa = rasa

    @abstractmethod
    def atack(self):
        pass

    def show_info(self):
        print(f"Name: {self.name}\nRasa: {self.rasa}")


class Human(AbstractBasePlayer):
    def __init__(self, name, age):
        super().__init__(name, "human")
        self.age = age

    def atack(self):
        print("Human atack with sword!")

    def show_info(self):
        # print("Human show_info with sword!")
        super().show_info()
        print(f"age : {self.age}")


class Elf(AbstractBasePlayer):
    def __init__(self, name):
        super().__init__(name, "elf")

    def atack(self):
        print("Elf atack with bowl!")


class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        if isinstance(player, AbstractBasePlayer) and player not in self.players:
            self.players.append(player)

    def show_players(self):
        if self.players:
            for player in self.players:
                player.show_info()

    def battle(self):
        if self.players:
            for player in self.players:
                player.atack()


h1 = Human("Max", 34)
h2 = Human("Bill", 54)

elf1 = Elf("Jin")

elf2 = Elf("Elfir")

game = Game()
game.add_player(elf1)
game.add_player(elf2)
game.add_player(h1)
game.add_player(h2)

game.show_players()
game.battle()

class pet:
    pass

print(type(type(pet)))

#METACLASS

class MyMetaClass(type):
    def __new__(cls, name, bases, dict):
        print("Hello from __new__()")
        print(f"type of the class created{cls}")
        print(f"Name: {name}")
        print(f"Bases: {bases}")
        print(f"Dict: {dict}")
        return super().__new__(cls,name,bases,dict)

class MyClas1(metaclass=MyMetaClass):
    attr = 100

class MyMetaClass1(type):
    def __new__(cls, name, bases, dict):
        if 'id' not in dict.keys():
            #print(f"No id attribute in class{cls}")
            print("add id attr")
            setattr(cls, "id" , id)
            return super().__new__(cls, name, bases, dict)
        else:
            methods = {key: value for key, value in dict.items() if callable(value)}
            if len(methods) > 2:
                print("error, more then 2 methods in class")
            else:
                print(f"Class: {name} is creating")
                return super().__new__(cls,name,bases,dict)

class MyClass1(metaclass=MyMetaClass1):
    attr = 100
    id = 0

class MyClass2(metaclass=MyMetaClass1):
    name = "asf"
    num = 0
    id = 0
    def method1(self):
        pass

    def method2(self):
        pass

    def method3(self):
        pass


#Завдання 1. Перший метаклас
#Створіть метаклас MyMeta, який під час створення нового класу виводить:
#Створюється клас: <назва класу>
#За допомогою цього метакласу створіть класи:
#class Student(metaclass=MyMeta):
#    passclass Teacher(metaclass=MyMeta):
#    pass
print("-" * 10)
class MyMeta(type):
    def __new__(cls, name, bases, dict):
        print(f"Створюєтся класс: {name}")
        return super().__new__(cls, name, bases, dict)

class Student(metaclass=MyMeta):
    pass

class Teacher(metaclass=MyMeta):
    pass

#Завдання 2. Обов'язковий метод
#Створіть метаклас RequiredMethodMeta.
#Він повинен перевіряти, чи містить створюваний клас метод:
#show_info()
#Якщо методу немає — заборонити створення класу за допомогою:
#raise TypeError(...)
print()
print("-" * 10)

class RequiredMethodMeta(type):
    def __new__(cls, name, bases, dict):
        if "show_info" not in dict:
            raise TypeError("Class dont have show_info()")
        else:
            print("Your class have method - show_info()")
            return super().__new__(cls, name, bases, dict)

class Student1(metaclass=RequiredMethodMeta):
    def show_info(self):
        pass