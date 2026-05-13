from src.models.exceptions import ValidationError


class User:
    def __init__(self, name, email):
        self.name = name
        self._email = email

    def set_email(self, email):
        if "@" not in email:
            raise ValidationError("Неверный формат email: должен быть @")
        if "." not in email:
            raise ValidationError("Неверный формат email: должна быть '.'")
        self._email = email
        print(f"Email установлен {email}")

    def get_email(self):
        return self._email