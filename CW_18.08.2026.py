import random


class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

        self.__person_id = random.randint(1,100)

    def get_info(self):
        self.__show_id()
        return f"{self.name} is {self._age} years old"

    def getHi(self, text):
        return f"{text}! I am {self.name}"

    def _get_name(self):
        return self.name

    def __show_id(self):
        print(self.__person_id)

person1 = Person("John", 20)
print(person1.getHi("Hi"))


class Student(Person):
    spec = "Computer science"

    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    def isSuccessfull(self):
        return True if self.score >= 75 else False

    def get_info(self):
        return super().get_info() + f" score is {self.score}"


student1 = Student("Bill", 20, 78)
print(student1.getHi("Hi"))
print(student1.get_info())
print(student1.isSuccessfull())

st2 = Student("Nick", 19, 45)
print(st2.getHi("Hi"))
print(st2.get_info())
print(st2.isSuccessfull())


class Employee(Person):
    def __init__(self, name, age, salary, jobTitle):
        super().__init__(name, age)
        self.salary = salary
        self.jobTitle = jobTitle

    def get_info(self):
        return super().get_info() + f" salary is {self.salary}, jobTitle is {self.jobTitle}"

    def change_age(self,new_age):
        self.new_age = self._age

print("_______")
p1 = Person("John", "32")
print(p1._get_name())


#1
#1) Створіть клас паспорт де будуть
# описані паспортні дані та на його основі створити загран паспорт

print("-------------")
class Passport:
    def __init__(self, name, surname, age, sex):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex

    def get_info(self):
        return f"Name: {self.name} | Surname: {self.surname} | Age: {self.age} | Sex: {self.sex}"


class Foreign(Passport):
    def __init__(self, name, surname, age, sex, nation):
        super().__init__(name, surname, age, sex)
        self.nation = nation

    def get_info(self):
        return super().get_info() + f" | Nation: {self.nation}"

pas1 = Passport("Nick", "Panchuk", 21, "M")
print("Звичайний паспорт:")
print(pas1.get_info())
print()

foreign = Foreign("Nick", "Panchuk", 21, "M", "Ukrainian")
print("Закордонний паспорт:")
print(foreign.get_info())

#2
#Завдання 2. Персонажі гри
#Створіть базовий клас:
#Character
#Атрибути:
#name health damage
#методи:
#show_info()attack()take_damage(amount)
#Потім створіть:
#Warrior(Character)Mage(Character)Archer(Character)
#Кожен клас повинен мати додатковий атрибут:
#warrior → armor
#Mage → mana
#Archer → arrows
#Перевизначте attack() для кожного персонажа:
#Warrior Alex attacks with

class Character:
    def __init__(self,name,health,damage):
        self.name = name
        self.health = health
        self.damage = damage

    def show_info(self):
        return f"Name: {self.name}| Health: {self.health}| Damage: {self.damage}"

    def attack(self):
        return f"{self.name} атакує і завдає {self.damage} шкоди"

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        return f"{self.name} отримує {amount} шкоди. Залишилось здоров'я: {self.health}"


class Warrior(Character):
    def __init__(self,name,health,damage,armor):
        super().__init__(name,health,damage)
        self.armor = armor

    def show_info(self):
        return super().show_info() + f"| Armor: {self.armor}"

    def attack(self):
        return f"Warrior {self.name} атакує мечем і завдає {self.damage} шкоди"

    def take_damage(self, amount):
        reduced = max(0, amount - self.armor)
        return super().take_damage(reduced)


class Mage(Character):
    def __init__(self,name,health,damage,mana):
        super().__init__(name,health,damage)
        self.mana = mana

    def show_info(self):
        return super().show_info() + f"| Mana: {self.mana}"

    def attack(self):
        if self.mana >= 50:
            self.mana -= 50
            return f"Mage {self.name} атакує магічним закляттям і завдає {self.damage} шкоди. (Залишок манни {self.mana}"
        else:
            return f"Mage {self.name} не достатньо мани для закляття"

class Archer(Character):
    def __init__(self,name,health,damage,arrows):
        super().__init__(name,health,damage)
        self.arrows = arrows

    def show_info(self):
        return super().show_info() + f"| Arrows: {self.arrows}"

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            return f"Archet {self.name} атакує с лука і завдає {self.damage} шкоди. (Залишилось стріл: {self.arrows})"
        else:
            return f"Archer {self.name} не має стріл для атаки"


print("=" * 40)
print("Warrior:")
warrior = Warrior("Tor", 100, 25, 10)
print(warrior.show_info())
print(warrior.attack())
print(warrior.take_damage(30))

print("\n" + "=" * 40)
print("Mage:")
mage = Mage("John", 70, 40, 70)
print(mage.show_info())
print(mage.attack())
print(mage.take_damage(20))

print("\n" + "=" * 40)
print("Archer:")
archer = Archer("Nick", 80, 30, 15)
print(archer.show_info())
print(archer.attack())
print(archer.take_damage(25))