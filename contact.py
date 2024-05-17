from name import Name
from phone import Phone

class Contact:
    """Клас для створення контактів."""
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phone = Phone(phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phone: {self.phone.value}"
