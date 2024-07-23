from decorator import input_error
from is_person_exist import is_person_exist


@input_error
def show_phone(args: list, contacts: list):
    name = args[0]

    if not is_person_exist(name, contacts):
        raise ValueError(f'The username with name {name} does not exist.')
    return next((person['phone'] for person in contacts if person['name'].lower() == args[0].lower()))
