class SFMShopException(Exception):
    """Базовое исключение для проекта SFMShop"""
    pass

class ValidationError(SFMShopException):
    """Ошибка валидации данных"""
    pass

class BusinessLogicError(SFMShopException):
    """Ошибка бизнес-логики"""
    pass

class DatabaseError(SFMShopException):
    """Ошибка базы данных"""
    pass

class NegativePriceError(ValidationError):
    """Цена не может быть отрицательной"""
    pass

class InsufficientStockError(BusinessLogicError):
    """Товара недостаточно на складе"""
    pass

class InvalidOrderError(BusinessLogicError):
    """Заказ невалиден"""
    pass
