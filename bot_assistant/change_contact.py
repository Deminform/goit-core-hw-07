from is_person_exist import is_person_exist
from is_valid_phone_number import is_valid_phone_number
from decorator import input_error


@input_error
def change_contact(args: list, contacts: list):

    name, phone = args
    if not is_valid_phone_number(phone):
        raise ValueError('Incorrect phone number.')

    if not is_person_exist(name, contacts):
        raise ValueError('The username not found.')

    for person in contacts:
        if person['name'].lower() == name.lower():
            person['phone'] = phone
            return 'Contact updated.'
