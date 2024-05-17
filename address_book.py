from collections import UserDict
from record import Record
from datetime import datetime, timedelta
import pickle

class AddressBook(UserDict):
    """Клас для зберігання та управління записами."""
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        """Додавання запису до адресної книги."""
        self.data[record.name.value] = record

    def search_record_by_name(self, name):
        """Пошук запису за іменем."""
        if name in self.data:
            return self.data[name]
        else:
            return None

    def delete_record_by_name(self, name):
        """Видалення запису за іменем."""
        if name in self.data:
            del self.data[name]
        else:
            print("Contact not found.")

    def get_upcoming_birthdays(self):
        """Отримати список користувачів, яких потрібно привітати на наступному тижні."""
        upcoming_birthdays = []
        today = datetime.now()
        for record in self.data.values():
            if record.birthday:
                birthday = record.birthday
                # Перевіряємо, чи день народження цього користувача відбудеться протягом наступного тижня
                if today < birthday < today + timedelta(days=7):
                    upcoming_birthdays.append(record)
        return upcoming_birthdays

    def __str__(self):
        contacts_info = []
        for record in self.data.values():
            phones_info = ', '.join(str(phone) for phone in record.phones)
            contact_info = f"Contact name: {record.name.value}, phones: {phones_info}"
            contacts_info.append(contact_info)
        return '\n'.join(contacts_info)