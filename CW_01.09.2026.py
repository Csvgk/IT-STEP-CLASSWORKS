"""
class DoubleNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_last(self,data):
        new_node = DoubleNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def show_forward(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def show_backward(self):
        current = self.tail

        while current is not None:
            print(current.data)
            current = current.prev


numbers = DoublyLinkedList()
numbers.add_last(30)
numbers.add_last(20)
numbers.add_last(10)
numbers.show_forward()
numbers.show_backward()


#1
#Завдання 1. Плейлист
#Створити двозв’язний список для пісень.
#Додати:
#Bohemian Rhapsody
#Believer
#Numb
#Take On Me
#Реалізувати:
#show_forward()
#show_backward()
#Очікуємо:
#Bohemian Rhapsody
#Believer
#Numb
#Take On Me
#та у зворотному порядку.
"""

class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_last(self, data):
        new_node = DoubleNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def show_forward(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def show_backward(self):
        current = self.tail
        while current is not None:
            print(current.data)
            current = current.prev

playlist = DoublyLinkedList()

playlist.add_last("Bohemian Rhapsody")
playlist.add_last("Believer")
playlist.add_last("Numb")
playlist.add_last("Take On Me")

print("Forward:")
playlist.show_forward()

print("\nBackward:")
playlist.show_backward()


#2
#Завдання 2. «Історія перегляду сторінок»
#Створіть програму, яка імітує історію перегляду сторінок у браузері за допомогою двозв’язного списку.
#Кожен вузол списку повинен зберігати:
#назву вебсторінки;
#посилання на наступний вузол;
#посилання на попередній вузол.
#Створіть клас Node для представлення одного вузла та клас BrowserHistory для роботи зі списком.
#Додайте до історії такі сторінки:
#Google ⇄ YouTube ⇄ GitHub ⇄ Wikipedia
#У класі BrowserHistory реалізуйте методи:
#1) add_page(page) — додає нову сторінку в кінець історії.
#2)show_forward() — проходить список від першої сторінки до останньої та виводить:
#Google
#YouTube
#GitHub
#Wikipedia
#3)show_backward() — проходить список у зворотному напрямку, від останньої сторінки до першої:
#Wikipedia
#GitHub
#YouTube
#Google
print()
class Node:
    def __init__(self, page):
        self.page = page
        self.next = None
        self.prev = None


class BrowserHistory:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_page(self, page):
        new_node = Node(page)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def show_forward(self):
        current = self.head
        while current is not None:
            print(current.page)
            current = current.next

    def show_backward(self):
        current = self.tail
        while current is not None:
            print(current.page)
            current = current.prev


history = BrowserHistory()

history.add_page("Google")
history.add_page("YouTube")
history.add_page("GitHub")
history.add_page("Wikipedia")

print("Forward:")
history.show_forward()

print("\nBackward:")
history.show_backward()


