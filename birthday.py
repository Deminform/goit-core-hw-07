import re
from datetime import datetime, date, timedelta
from field import Field


class Birthday(Field):

    def __init__(self, value):
        try:
            if isinstance(value, str) and re.match(r'^\d{2}.\d{2}.\d{4}$', value):
                value = datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

        super().__init__(value.date().strftime('%d.%m.%Y'))

    # @staticmethod
    # def string_to_date(date_string):
    #     return datetime.strptime(date_string, '%d.%m.%Y').date()
    #
    # @staticmethod
    # def date_to_string(value):
    #     return value.strftime('%d.%m.%Y')
    #
    # def prepare_user_list(self, user_data):
    #     prepared_list = []
    #     for user in user_data:
    #         prepared_list.append({"name": user["name"], "birthday": self.string_to_date(user["birthday"])})
    #     return prepared_list
    #
    # @staticmethod
    # def find_next_weekday(start_date, weekday):
    #     days_ahead = weekday - start_date.weekday()
    #     if days_ahead <= 0:
    #         days_ahead += 7
    #     return start_date + timedelta(days=days_ahead)
    #
    # def adjust_for_weekend(self, birthday):
    #     if birthday.weekday() >= 5:
    #         return self.find_next_weekday(birthday, 0)
    #     return birthday
    #
    # def get_upcoming_birthdays(self, users, days=7):
    #     upcoming_birthdays = []
    #     today = date.today()
    #
    #     for user in users:
    #         birthday_this_year = user["birthday"].replace(year=today.year)
    #
    #         if birthday_this_year < today:
    #             birthday_this_year = user["birthday"].replace(year=today.year + 1)
    #
    #         if 0 <= (birthday_this_year - today).days <= days:
    #             birthday_this_year = self.adjust_for_weekend(birthday_this_year)
    #
    #             congratulation_date_str = self.date_to_string(birthday_this_year)
    #             upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
    #     return upcoming_birthdays
