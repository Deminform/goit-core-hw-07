from collections import UserDict
from record import Record
from prettytable import PrettyTable


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.data = {}

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return next((record for record in self.data.values() if record.name.value == name), None)

    def delete(self, name: str):
        if name in self.data.keys():
            del self.data[name]

    def __str__(self):
        table = PrettyTable()
        table.align = 'l'
        table.field_names = ["#", "Name", "Phones"]

        for index, record in enumerate(self.data.values(), start=1):
            phones = ", ".join(phone.value for phone in record.phones)
            table.add_row([index, record.name.value, phones])

        return table.get_string()
