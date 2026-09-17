"""
import threading
import time


#
# print("test 1")
# print("test 2")
#
# print(threading.current_thread().name)
#
# def work():
#     print(f"start work {threading.current_thread().name}")
#     time.sleep(2)
#     print(f"end work {threading.current_thread().name}")
#
# thread1 = threading.Thread(target=work)
# thread1.start()
# thread1.join()

def download(filename):
    print("start")
    print("download", filename)
    time.sleep(3)
    print("finish")


# thread = threading.Thread(target=download, args=("download.txt",))
# thread.start()
# thread.join()

# start = time.perf_counter()
# download("test.txt")
# download("test.txt")
# download("test.txt")
#
# print(time.perf_counter() - start)
#
# start = time.perf_counter()
# t1 = threading.Thread(target=download, args=("test.txt",))
# t2 = threading.Thread(target=download, args=("photo.jpg",))
# t3 = threading.Thread(target=download, args=("audio.mp3",))
#
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()
# print(time.perf_counter() - start)
# print("End working program")


# balance = 1000
#
# lock = threading.Lock()
#
#
# def withdraw(name, amount):
#     global balance
#     with lock:
#         print("check balance")
#         if amount <= balance:
#             time.sleep(1)
#             balance -= amount
#             print(name, 'get', amount)
#         else:
#             print(name, 'not enough money')
#
#
# t1 = threading.Thread(target=withdraw, args=("Anna", 700))
# t2 = threading.Thread(target=withdraw, args=("Max", 500))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print(balance)

from queue import Queue

tasks = Queue()


#
# while not tasks.empty():
#
#     task = tasks.get()
#     print(task)
#     tasks.task_done()
#
#
# print("waiting..")
# tasks.join()
# print("All tasks done")


def worker():
    while True:
        task = tasks.get()
        print("start task", task)
        time.sleep(2)
        print("end task", task)
        tasks.task_done()

#
# thread = threading.Thread(target=worker)
# thread.start()
# for i in range(3):
#     t = threading.Thread(target=worker)
#     t.start()
#
# tasks.put("photo.ipg")
# tasks.put("music.mp3")
# tasks.put("music.mp4")
# print("all tasks added")
#
# tasks.join()

from multiprocessing import Process
import os

def work():
    print("p id", os.getpid())

if __name__ == "__main__":
    print("main id", os.getpid())
    p1 = Process(target=work)
    p2 = Process(target=work)
    time.sleep(30)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

"""
#Завдання 1
#Користувач вводить з клавіатури значення у список. Після чого запускаються два потоки.
#Перший потік знаходить максимум у списку. Другий потік знаходить мінімум у списку.
#Результати обчислень виведіть на екран.

import threading

def find_max(lst):
    maximum = max(lst)
    print("Максимум у списку:", maximum)

def find_min(lst):
    minimum = min(lst)
    print("\nМінімум у списку:", minimum)

n = int(input("Скільки чисел буде у списку? "))
numbers = []
for i in range(n):
    num = float(input(f"Введіть число {i+1}: "))
    numbers.append(num)

print("Список:", numbers)

t1 = threading.Thread(target=find_max, args=(numbers,))
t2 = threading.Thread(target=find_min, args=(numbers,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Роботу завершено")

#Завдання 2
#Користувач вводить з клавіатури значення у список. Після чого запускаються два потоки.
#Перший потік знаходить суму елементів у списку. Другий потік знаходить середнє арифметичне у списку.
#Результати обчислень виведіть на екран.

import threading

def find_sum(lst):
    total = sum(lst)
    print("Сума елементів:", total)

def find_average(lst):
    if len(lst) == 0:
        print("Середнє арифметичне: список порожній")
        return
    avg = sum(lst) / len(lst)
    print("Середнє арифметичне:", avg)

n = int(input("Скільки чисел буде у списку? "))
numbers = []
for i in range(n):
    num = float(input(f"Введіть число {i+1}: "))
    numbers.append(num)

print("Список:", numbers)

t1 = threading.Thread(target=find_sum, args=(numbers,))
t2 = threading.Thread(target=find_average, args=(numbers,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Роботу завершено")

#Завдання 3
#Користувач вводить з клавіатури шлях до файлу, що містить набір чисел. Після чого запускаються два потоки.
#Перший потік створює новий файл, в який запише лише парні елементи списку.
#Другий потік створює новий файл, в який запише лише непарні елементи списку.
#Кількість парних і непарних елементів виводиться на екран.

import threading

def write_even(numbers, filename="even.txt"):
    even = [x for x in numbers if x % 2 == 0]
    with open(filename, "w", encoding="utf-8") as f:
        for num in even:
            f.write(str(num) + "\n")
    print(f"Кількість парних елементів: {len(even)}")
    print(f"Парні числа записано у файл {filename}")

def write_odd(numbers, filename="odd.txt"):
    odd = [x for x in numbers if x % 2 != 0]
    with open(filename, "w", encoding="utf-8") as f:
        for num in odd:
            f.write(str(num) + "\n")
    print(f"Кількість непарних елементів: {len(odd)}")
    print(f"Непарні числа записано у файл {filename}")

filepath = input("Введіть шлях до файлу з числами: ")

numbers = []
try:
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                numbers.append(int(line))
except FileNotFoundError:
    print("Файл не знайдено!")
    exit()
except ValueError:
    print("У файлі є некоректні дані (не числа)!")
    exit()

print("Прочитані числа:", numbers)

t1 = threading.Thread(target=write_even, args=(numbers,))
t2 = threading.Thread(target=write_odd, args=(numbers,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Роботу завершено")