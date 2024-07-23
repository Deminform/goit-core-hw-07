from decorator import input_error
from prettytable import PrettyTable


@input_error
def show_all(contacts: list):
    table = PrettyTable()
    table.align = 'l'
    table.field_names = ['Name', 'Phone number', 'id']

    for person in contacts:
        table.add_row([person['name'], person['phone'], person["id"]])
    return 'No records yet' if len(contacts) == 0 else table
