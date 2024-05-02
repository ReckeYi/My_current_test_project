from faker import Faker
from datetime import timezone


class RandomVariables:
    def __init__(self):
        self.fake = Faker('ru_RU')

    def random_date(self):
        return self.fake.date_time_this_decade(tzinfo=timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    def random_department_name(self):
        return self.fake.text()

    def random_topic_title(self):
        return self.fake.text(max_nb_chars=18)

    def random_first_name(self):
        return self.fake.first_name()

    def random_last_name(self):
        return self.fake.last_name()

    def random_middle_name(self):
        return self.fake.last_name()

    def random_text_200(self, length=200):
        return self.fake.text(max_nb_chars=length)

    def random_text_50(self, length=50):
        return self.fake.text(max_nb_chars=length)

    def random_email(self):
        return self.fake.email()

    def random_phone_number(self):
        phone_number_without_prefix = str(self.fake.random_number(digits=7, fix_len=True))
        phone_number = "+7978" + phone_number_without_prefix
        return phone_number

    def random_address(self):
        return self.fake.address()


random_variables = RandomVariables()
random_date = random_variables.random_date()
random_department_name = random_variables.random_department_name()
random_topic_title = random_variables.random_topic_title()
random_first_name = random_variables.random_first_name()
random_last_name = random_variables.random_last_name()
random_middle_name = random_variables.random_middle_name()
random_text_200 = random_variables.random_text_200()
random_text_50 = random_variables.random_text_50()
random_email = random_variables.random_email()
random_phone_number = random_variables.random_phone_number()
random_address = random_variables.random_address()