from input_parsing import parse_input
from file_handling import save_data, load_data
from address_book import AddressBook
from contact import Contact
from record import Record 
from datetime import datetime


def input_error(func):
    """Декоратор для обробки помилок вводу."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
    return wrapper

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.search_record_by_name(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        # Видалення пробілів і символів роздільників з номера телефону
        cleaned_phone = ''.join(filter(str.isdigit, phone))
        # Додавання телефонного номеру до запису
        record.add_phone(cleaned_phone)
    return message

@input_error
def change_phone(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.search_record_by_name(name)
    if record:
        # Видалення пробілів і символів роздільників з номерів телефонів
        cleaned_old_phone = ''.join(filter(str.isdigit, old_phone))
        cleaned_new_phone = ''.join(filter(str.isdigit, new_phone))
        record.edit_phone(cleaned_old_phone, cleaned_new_phone)
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(args, book: AddressBook):
    name, *_ = args
    record = book.search_record_by_name(name)
    if record:
        phones_info = ', '.join(record.phones)
        return f"Phone numbers for contact '{name}': {phones_info}"
    else:
        return "Contact not found."

@input_error
def show_all_contacts(book: AddressBook):
    if book:
        return str(book)
    else:
        return "No contacts available."

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.search_record_by_name(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        return "Contact not found."

@input_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    record = book.search_record_by_name(name)
    if record:
        if record.birthday:
            return f"Birthday for contact '{name}': {record.birthday.value.strftime('%d.%m.%Y')}"
        else:
            return f"Contact '{name}' does not have a birthday set."
    else:
        return "Contact not found."

@input_error
def show_upcoming_birthdays(book: AddressBook):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        return '\n'.join([f"{record.name.value}: {record.birthday.value.strftime('%d.%m.%Y')}" for record in upcoming_birthdays])
    else:
        return "No upcoming birthdays."



def main():
    address_book = load_data()  # Завантаження адресної книги з файлу
    print("Welcome to the assistant bot!")
    print("You can use some of these commands:\n add [name] [phone number] \n change [name] [new phone number] \n phone [name] \n all \n add-birthday [name] [DD.MM.YYYY] \n show-birthday [name] \n birthdays \n close or exit. \n Let's go!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            save_data(address_book)  # Збереження адресної книги у файл
            break

        elif command == "add":
            if len(args) != 2:
                print("Invalid command syntax. Use: add [name] [phone number]")
                continue
            name, phone = args
            if address_book.search_record_by_name(name):
                address_book.search_record_by_name(name).add_phone(phone)
                print(f"Phone number added to existing contact '{name}'.")
            else:
                contact = Contact(name, phone)
                address_book.add_record(Record(name))
                print(f"New contact '{name}' added with phone number {phone}.")

        elif command == "change":
            if len(args) != 2:
                print("Invalid command syntax. Use: change [name] [new phone number]")
                continue
            name, new_phone = args
            record = address_book.search_record_by_name(name)
            if record:
                record.add_phone(new_phone)
                print(f"Phone number changed for contact '{name}'.")
            else:
                print(f"Contact '{name}' not found.")

        elif command == "phone":
            if len(args) != 1:
                print("Invalid command syntax. Use: phone [name]")
                continue
            name = args[0]
            record = address_book.search_record_by_name(name)
            if record:
                print(f"Phone numbers for contact '{name}':")
                for phone in record.phones:
                    print(phone)
            else:
                print(f"Contact '{name}' not found.")

        elif command == "all":
            print("All contacts in the address book:")
            print(address_book)

        elif command == "add-birthday":
            if len(args) != 2:
                print("Invalid command syntax. Use: add-birthday [name] [DD.MM.YYYY]")
                continue
            name, birthday = args
            record = address_book.search_record_by_name(name)
            if record:
                try:
                    birthday_date = datetime.strptime(birthday, "%d.%m.%Y")
                    record.birthday = birthday_date
                    print(f"Birthday added to contact '{name}'.")
                except ValueError:
                    print("Invalid date format. Use DD.MM.YYYY")
            else:
                print(f"Contact '{name}' not found.")

        elif command == "show-birthday":
            if len(args) != 1:
                print("Invalid command syntax. Use: show-birthday [name]")
                continue
            name = args[0]
            record = address_book.search_record_by_name(name)
            if record and record.birthday:
                print(f"Birthday for contact '{name}': {record.birthday.strftime('%d.%m.%Y')}")
            elif record:
                print(f"Contact '{name}' does not have a birthday set.")
            else:
                print(f"Contact '{name}' not found.")

        elif command == "birthdays":
            upcoming_birthdays = address_book.get_upcoming_birthdays()
            if upcoming_birthdays:
                print("Upcoming birthdays:")
                for record in upcoming_birthdays:
                    print(f"{record.name.value}: {record.birthday.strftime('%d.%m.%Y')}")
            else:
                print("No upcoming birthdays.")

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()