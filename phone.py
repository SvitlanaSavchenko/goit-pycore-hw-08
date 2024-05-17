from field import Field

class Phone(Field):
    """Клас для зберігання номера телефону. Має валідацію формату (10 цифр)."""
    def __init__(self, value):
        # Видаляємо пробіли та інші роздільники з номера телефону
        cleaned_value = ''.join(filter(str.isdigit, value))
        super().__init__(cleaned_value)
        if not self.validate_phone():
            raise ValueError("Invalid phone number format.")

    def validate_phone(self):
        """Перевіряє правильність формату номера телефону."""
        try:
            if len(self.value) < 1:
                raise ValueError("The phone number cannot be empty")
            if len(self.value) != 10 and not (len(self.value) == 12 and self.value[0] == '+'):
                raise ValueError("The phone number must contain 10 digits or start with '+' and have 11 digits")
            if not self.value.isdigit() and not self.value[1:].isdigit():
                raise ValueError("The phone number must contain only numbers")
        except ValueError as e:
            print(e)
            return False
        return True


    def __eq__(self, other):
        """Магічний метод для порівняння об'єктів класу Phone за їхнім значенням."""
        if isinstance(other, Phone):
            return self.value == other.value
        return False