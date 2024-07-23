import re
from add_contact import add_contact
from parse_input import parse_input
from change_contact import change_contact
from show_phone import show_phone
from show_all import show_all
from decorator import input_error
from adress_book import AddressBook


@input_error
def main():
    book = AddressBook()
    print('Welcome to the assistant bot!')
    print('Available commands: add name phone / change name phone / phone name / all')
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        if command in ['close', 'exit']:
            print("Good bye!")
            break
        elif command in ['hello', 'hi']:
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args, book))
        elif command == 'change':
            print(change_contact(args, book))
        elif command == 'phone':
            print(show_phone(args, book))
        elif command == 'all':
            print(show_all(book))
        else:
            print('Invalid command.')


if __name__ == '__main__':
    main()
