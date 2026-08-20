import random
import datetime


class Person:
    hobby = ""

    def __init__(self, name, age):
        if Person.validate_name(name):
            self.name = name
        # protected prop
        self._age = age
        # private prop
        self.__person_id = random.randint(1, 100)

    def get_info(self):
        self.__show_id()
        return f"{self.name} is {self._age} years old"

    def _get_name(self):
        return self.name

    def __show_id(self):
        print(self.__person_id)

    @staticmethod
    def getHi(text):
        return f"{text}!"

    @staticmethod
    def is_adult(age):
        return age >= 18

    @staticmethod
    def validate_name(name):
        return len(name) >= 2

    def show_name(self):
        if Person.validate_name(self.name):
            print(self.name)

    @classmethod
    def setDefaulteHobby(cls, hobby):
        cls.hobby = hobby

    @classmethod
    def basedOnYear(cls, name, bYear):
        personAge = datetime.date.today().year - bYear
        return cls(name, personAge)


p1 = Person("John", 20)
print(p1.getHi("hello"))
print(Person.getHi("test class"))

print(Person.is_adult(20))

newpwerson = Person.basedOnYear('max', 2005)

print(newpwerson.get_info())
Person.setDefaulteHobby("Cooking")
print(newpwerson.hobby)


class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b


print(Math.add(3, 4))

math = Math()


class MyBook:
    def __init__(self, title, auther, pages):
        self.title = title
        self.auther = auther
        self.pages = pages

    def get_info(self):
        print(self.title)
        print(self.auther)
        print(self.pages)


class MyFile:
    def __init__(self, file_size, src):
        self.file_size = file_size
        self.src = src

    def get_info(self):
        print(self.file_size)
        print(self.src)


class MyEBook(MyBook, MyFile):
    def __init__(self, title, auther, pages, file_size, src):
        MyBook.__init__(self, title, auther, pages)
        MyFile.__init__(self, file_size, src)
        self.price = 0

    def get_info(self):
        MyBook.get_info(self)
        MyFile.get_info(self)


eBook1 = MyEBook('python', 'Gvido', 356, 2, 'location')
eBook1.get_info()
#Завдання 3
#Створіть два батьківські класи:
#Клас Phone:
#phone_number — номер телефону;
#метод call(number) — виводить повідомлення про дзвінок;
#метод show_phone_info() — показує номер телефону.
#Клас Camera:
#megapixels — кількість мегапікселів;
#метод take_photo() — виводить повідомлення про створення фотографії;
#метод show_camera_info() — показує характеристики камери.
#Створіть клас:
#class Smartphone(Phone, Camera):
#Він повинен успадковувати можливості одночасно від Phone і Camera.
#У Smartphone додайте власні атрибути:
#brandmodel
#та метод:
#show_info()
print("-------------")
class Phone:
    def __init__(self,phone_number):
        self.number = phone_number

    def call(self,number):
        print(f"Вам дзвонять на номер - {self.number}")

    def show_phone_info(self):
        print(f"Ваш номер телефону {self.number}")

class Camera:
    def __init__(self,megapixels):
        self.megapixels = megapixels

    def take_photo(self):
        print(f"Ви зробили фото")

    def show_camera_info(self):
        print(f"Телефон має {self.megapixels} МП")

class Smartphone(Phone, Camera):
    def __init__(self,phone_number,megapixels,brand,model):
        Phone.__init__(self,phone_number)
        Camera.__init__(self,megapixels)
        self.brand = brand
        self.model = model

    def show_info(self):
        Phone.show_phone_info(self)
        Camera.show_camera_info(self)
        print(self.brand)
        print(self.model)


phone1 = Smartphone("+380 066 031 32 21", 12, "iPhone", "17 Pro")
phone1.show_info()