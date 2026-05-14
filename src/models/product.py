from src.models.exceptions import ValidationError


class Product:
    def __init__(self, name, price, quantity, stock=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.stock = stock

    def set_price(self, price):
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        self.price = price

    def __str__(self):
        return f"Товар: {self.name}, Цена: {self.price} руб., Количество: {self.quantity}"

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price

    def apply_discount(self):
        pass

    def check_stock(self):
        return self.stock

    def update_stock(self, quantity):
        if quantity < 0:
            raise ValueError("Количество не может быть меньше ноля")
        self.stock = quantity
        print(f"Склад обновлён: '{self.name}', остаток: {self.stock}")
        