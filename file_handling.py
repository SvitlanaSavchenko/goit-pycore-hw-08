import pickle
from address_book import AddressBook

def save_data(book, filename="addressbook.pkl"):
    """Зберегти адресну книгу в файл."""
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    """Завантажити адресну книгу з файлу."""
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернути нову адресну книгу, якщо файл не знайдено