from colorama import Fore, Style, init
from decorator import input_error
from is_person_exist import is_person_exist


@input_error
def show_phone(args: list, contacts: list):
    init(autoreset=True)

    name = args[0]

    if not is_person_exist(name, contacts):
        raise ValueError(Fore.YELLOW + f'The username with name {name} does not exist.')

    return next((person['phone'] for person in contacts if person['name'].lower() == args[0].lower()))
