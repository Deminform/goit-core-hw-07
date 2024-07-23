from field import Field
import re


class Phone(Field):
    def __init__(self, value):
        """ Check if the number is correct """
        try:
            if re.match(r'^\d{10}$', value):
                super().__init__(value)
        except ValueError:
            raise ValueError("Invalid phone number. Must contain 10 digits.")
