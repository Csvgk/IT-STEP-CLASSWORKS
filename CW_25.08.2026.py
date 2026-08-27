"""
print("positive")
print(123)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Max", 18)
print(person1)

print(2 + 2)
print("2" + "2")


# print("2" + 2)


class Film:
    def __init__(self, title, director, age):
        self.title = title
        self.director = director
        self.age = age

    def showInfo(self):
        print(self.title)
        print(self.director)
        print(self.age)

    def __str__(self):
        return f"{self.title} {self.director} {self.age}"


class Book:
    def __init__(self, title, director, pages):
        self.title = title
        self.director = director
        self.pages = pages

    def showInfo(self):
        print(self.title)
        print(self.director)
        print(self.pages)

    def __str__(self) -> str:
        return f"{self.title} {self.director}, {self.pages}"

    def __gt__(self, other):
        return self.pages > other.pages

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.director == other.director
        else:
            return False


film1 = Film("Python", "Max", 18)
book1 = Book("qwerty", "Bill", 150)
book2 = Book("qwerty", "Bill2", 50)
for item in (film1, book1):
    # item.showInfo()
    print(item)

print(book1 == book2)


class Class1:
    def __new__(cls):
        print("Hi i am __new__ magic method!")
        return super(Class1, cls).__new__(cls)

    def __init__(self):
        print("Hi i am __init__ magic method!")


obj1 = Class1()
print(book1 > book2)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x} : {self.y})"

    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        elif isinstance(other, int):
            return Point(self.x * other, self.y * other)
        else:
            raise TypeError("error multiplication")

    def __iadd__(self, other):
        if isinstance(other, int):
            self.x += other
            self.y += other
            return self
        elif isinstance(other, Point):
            self.x += other.x
            self.y += other.y
            return self
        else:
            raise TypeError("error addition")


p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1)
print(p2)
print(p1 * p2)
print(p1 * 2)
# print(p1 * 3.5)

a = 1
a += 10
print(a)
print(p1)
p1 += p2
print(f"{p1}")

print(2 + "4")

"""
#Завдання 1
#Створіть (або використайте раніше створений) клас «Число».
# Клас «Число» зберігає всередині одне значення.
#Використовуючи перевантаження операторів,
# реалізуйте для нього арифметичні операції для роботи з числом (операції +, -, *, /).

class Numeric:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x} : {self.y})"

    def __mul__(self, other):
        if isinstance(other, Numeric):
            return Numeric(self.x * other.x, self.y * other.y)
        elif isinstance(other, int):
            return Numeric(self.x * other, self.y * other)
        else:
            raise TypeError("error multiplication")

    def __add__(self, other):
        if isinstance(other, Numeric):
            return Numeric(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Numeric(self.x + other, self.y + other)
        else:
            raise TypeError("error addition")

    def __sub__(self, other):
        if isinstance(other, Numeric):
            return Numeric(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Numeric(self.x - other, self.y - other)
        else:
            raise TypeError("error subtraction")

    def __truediv__(self, other):
        if isinstance(other, Numeric):
            if other.x == 0 or other.y == 0:
                raise ZeroDivisionError("division by zero")
            return Numeric(self.x / other.x, self.y / other.y)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("division by zero")
            return Numeric(self.x / other, self.y / other)
        else:
            raise TypeError("error division")

n1 = Numeric(10, 20)
n2 = Numeric(2, 5)

print(n1)
print(n2)

print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)

print(n1 + 3)
print(n1 * 2)
print(n1 / 2)

#Завдання 2
#Створіть клас «Бібліотека». Клас призначений для збереження інформації про бібліотеку
# (назва, адреса, кількість книг і т.д.). Реалізуйте потрібні для класу способи.
# Використовуючи перевантаження операторів, реалізуйте для нього наступні арифметичні операції:
# + — додає до кількості книг вказане значення;
# - — віднімає з кількості книг вказане значення;
# += —додає до кількості книг вказане значення;
# -= — віднімає з кількості книг вказане значення.
# Використовуючи перевантаження операторів, реалізуйте (порівняння за кількістю книг):
# <;
# ;
# =;
# =;
# =;
# !=.

class Library:
    def __init__(self,name,address,book_count):
        self.name = name
        self.address = address
        self.book_count = book_count

    