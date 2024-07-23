from name import Name
from phone import Phone
from birthday import Birthday


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    ''' Work with birthday field 
        Methods: 
        - add_birthday
        - show_birthday
    '''

    # @input_error
    def add_birthday(self, value: str):
        self.birthday = Birthday(value)

    def show_birthday(self):
        return self.birthday

    ''' Work with phone field 
        Methods: 
        - add
        - remove
        - edith
        - find
    '''

    def add_phone(self, phone_number: str):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)

    def edit_phone(self, phone_number: str, new_phone_number: str):
        self.remove_phone(phone_number)
        self.add_phone(new_phone_number)

    def find_phone(self, phone_number: str):
        return next((phone for phone in self.phones if phone.value == phone_number), None)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
