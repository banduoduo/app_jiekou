from faker import Faker


class ContactInfoAdd:
    def __init__(self):
        self.faker = Faker('zh-CN')

    def add_name(self):
        name = self.faker.name()
        return name

    def add_phone(self):
        phone_num = self.faker.phone_number()
        return phone_num


if __name__ == '__main__':
    con = ContactInfoAdd()
    print(con.add_phone())
    print(con.add_name())
