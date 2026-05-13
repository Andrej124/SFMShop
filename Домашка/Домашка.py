"""ЧИСЛА"""
'''
# Заказ 1: с обычной скидкой
order_1_price = 2000.0
order_1_quantity = 2
order_1_discount = 0.15

# Заказ 2: без скидки
order_2_price = 3000.0
order_2_quantity = 1
order_2_discount = 0.0

# Заказ 3: с большой суммой
order_3_price = 5000.0
order_3_quantity = 3
order_3_discount = 0.2

final_price1 = order_1_price * order_1_quantity * (1 - order_1_discount)
print("Заказ 1:")
print("Исходная цена:", order_1_price * order_1_quantity, "руб.")
print("Размер скидки:", (order_1_price * order_1_quantity) * order_1_discount, "руб.")
print("Итоговая стоимость:", round(final_price1, 2), "руб.\n")

final_price2 = order_2_price * order_2_quantity * (1 - order_2_discount)
print("Заказ 2:")
print("Исходная цена:", order_2_price * order_2_quantity, "руб.")
print("Размер скидки:", (order_2_price * order_2_quantity) * order_2_discount, "руб.")
print("Итоговая стоимость:", round(final_price2, 2), "руб.\n")

final_price3 = order_3_price * order_3_quantity * (1 - order_3_discount)
print("Заказ 3:")
print("Исходная цена:", order_3_price * order_3_quantity, "руб.")
print("Размер скидки:", (order_3_price * order_3_quantity) * order_3_discount, "руб.")
print("Итоговая стоимость:", round(final_price3, 2), "руб.")'''

"""Условные операторы"""
'''
order_total = 6000

if order_total < 0:
    print("Ошибка: сумма заказа не может быть меньше 0!")
elif order_total > 10000:
    discount_rate = 0.15  # 15%
elif order_total > 5000:
    discount_rate = 0.10  # 10%
else:
    discount_rate = 0.05  # 5%

print("Исходная сумма заказа:", order_total, "руб.")
print("Размер скидки:", discount_rate * 100, "%", "руб.")
print("Размер скидки:", order_total - (order_total * (1 - discount_rate)), "руб.")
print("Итоговая стоимость:", round(order_total * (1 - discount_rate)), "руб.")
'''

"""Циклы (for, while)"""
'''
price_1 = 500
price_2 = 1500
price_3 = 800
price_4 = 2000
price_5 = 1200

count = 0
max_price = 0
max_price_index = 0

for i in range(1, 6):
    if i == 1:
        total = price_1
    elif i == 2:
        total = price_2
    elif i == 3:
        total = price_3
    elif i == 4:
        total = price_4
    else:
        total = price_5

    if total > 1000:
        print("Заказ", i, ":", total)
        count += 1

    if total > max_price:
        max_price = total
        max_price_index = i

if count == 0:
    print("Товаров с ценой больше 1000 руб не найдено.")
else:
    print("Количество товаров с ценой больше 1000:", count)
    print("Товар с максимальной ценой:", max_price_index)
'''
"""Списки (list)"""
'''
prices = [1500, 2300, 890, 4500, 1200]

prices.sort(reverse=True)
print("Отсортированный список", prices)
print("Максимальная цена:", max(prices))
print("Минимальная цена:", min(prices))
'''
'''
cart = []

cart.append(["Ноутбук", 50000])
cart.append(["Мышь", 1500])
cart.append(["Клавиатура", 3000])
print("Корзина после добавления товаров:", cart)

cart.remove(["Мышь", 1500])
print("Корзина после удаления:", cart)

cart.sort()
print("Корзина после сортировки:", cart)

if len(cart) > 0:
    max_price = 0
    max_price_item = None

    for item in cart:
        price = item[1]
        if price > max_price:
            max_price = price
            max_price_item = item
    print("Самый дорогой товар:", max_price_item)
else:
    print("Корзина пустая")
'''
"""Функции"""
'''
def calculate_order_total(price, quantity, discount):
    total_price = (price * quantity) * (1 - discount)
    return total_price

def check_stock_availability(stock_quantity, required_quantity):
    if stock_quantity >= required_quantity:
        return True
    else:
        return False

def format_order_info(order_id, total):
    info = "Заказ #" + str(order_id) + ", Сумма: " + str(total) + " руб."
    return info

calculate_total = calculate_order_total(1000, 3, 0.1)
stock_total = check_stock_availability(10, 3)
info_total = format_order_info(1, calculate_total)

print(calculate_total)
print("Товар доступен:", stock_total)
print("Информация о заказе:", info_total)
'''

"""СЛОВАРИ И МНОЖЕСТВА"""

'''Задание 1: Работа со словарем товара'''
'''
product = {
    "name" : "Ноутбук",
    "price" : "50000",
    "quantity" : "5"
}

product.update({"quantity" : "10"})
keys = product.keys()
values = product.values()

print(keys)
print(values)
'''

"""Система хранения данных о пользователях и товарах"""
'''
users = {}
products = {
    "Ноутбук": {"price": 50000, "category": "Компьютерные товары"}
}

visitors = set()

users[1] = {
    'name': 'Иван',
    'email': 'ivan@test.com'
}
print(f"Пользователь добавлен, {users[1]}")

if "Ноутбук" in products:
    print(f"Цена товара 'Ноутбук': {products["Ноутбук"]["price"]} руб.")
else:
    print("Товар не найден")

visitors.add("user_123")
visit_true_or_false = "user_123" in visitors
if "user_123" in visitors:
    print(f"Посетитель 'user_123' был на сайте: {visit_true_or_false}")
'''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""ООП"""
''Задание 1: Создание класса Product'''
'''
class Product:
    def __init__(self,name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity
    
    def get_info(self):
        return "Товар: " + self.name + ", Цена: " + str(self.price) + ", Количество: " + str(self.quantity)

laptop = Product("Ноутбук", 50000, 10)


total = laptop.get_total_price()
info = laptop.get_info()
print("Общая стоимость товара:", total, "руб.")
print(info)
'''
''''''''''''''''''''''''''''''''''''''''''''
"""ООП"""
'''Исключения'''
'''Задание 1: Обработка ошибок деления'''
'''
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
    except TypeError:
        print("Ошибка: неверный тип данных!")
    

print("Результат:", divide(10, 2))
print(divide(10, 0))
print(divide(4, "b"))
'''
'''Собственные исключения'''
'''
class MyCustomError(Exception):
    pass

def age_18_or_not(age):
    if age < 18:
        raise MyCustomError("Ошибка! Возраст должен быть больше 18 лет!")
    return age

try:
    result_age = age_18_or_not(18)
    print("Проверка по возрасту успешно пройдена!")
except MyCustomError as e:
        print(f"Обработано исключение: {e}")
'''




