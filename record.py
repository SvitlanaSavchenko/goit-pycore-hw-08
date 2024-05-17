from name import Name
from phone import Phone
from birthday import Birthday

class Record:
    """Клас для зберігання інформації про контакт, включаючи ім'я, список телефонів та день народження."""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        # Додавання нового телефонного номеру до запису
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            print("Phone number not found.")

    def find_phone(self, phone):
        # Пошук телефонного номеру у записі
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj.value
        raise ValueError("Phone number not found in record.")

    def edit_phone(self, old_phone, new_phone):
        # Редагування існуючого телефонного номеру у записі
        for phone_obj in self.phones:
            if phone_obj.value == old_phone:
                phone_obj.value = new_phone
                break
        else:
            raise ValueError("Phone number not found in record.")

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones_info = ', '.join(str(phone) for phone in self.phones)
        birthday_info = f", birthday: {self.birthday.value.strftime('%d.%m.%Y')}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones_info}{birthday_info}"
