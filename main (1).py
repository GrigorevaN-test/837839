#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
example.py - учебный скрипт на Python
Демонстрирует основные возможности языка
"""

# Импорт модулей
import math
from datetime import datetime

# Константа
PI = 3.14159

# Функция с типизацией (Python 3.6+)
def calculate_circle_area(radius: float) -> float:
    """Вычисляет площадь круга"""
    return PI * (radius ** 2)

# Класс
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def greet(self):
        """Приветствие"""
        print(f"Привет! Меня зовут {self.name}, мне {self.age} лет.")

# Основной код
if __name__ == "__main__":
    print("="*40)
    print(f"Запуск программы: {datetime.now()}")
    print("="*40)
    
    # Работа с функцией
    radius = 5.0
    area = calculate_circle_area(radius)
    print(f"Площадь круга с радиусом {radius} = {area:.2f}")
    
    # Работа с классом
    person = Person("Иван", 30)
    person.greet()
    
    # Пример работы со списком
    fruits = ["яблоко", "банан", "апельсин"]
    print("\nСписок фруктов:")
    for i, fruit in enumerate(fruits, 1):
        print(f"{i}. {fruit.capitalize()}")
    
    # Пример работы со словарем
    print("\nКвадраты чисел:")
    squares = {x: x**2 for x in range(1, 6)}
    for num, square in squares.items():
        print(f"{num}² = {square}")
