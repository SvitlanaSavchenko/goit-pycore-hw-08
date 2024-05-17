from field import Field
from datetime import datetime

class Birthday(Field):
    """Клас для зберігання дня народження."""
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")