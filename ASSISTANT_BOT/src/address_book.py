from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        value = str(value)

        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone must contain 10 digits")

        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def remove_phone(self, phone):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)

    def edit_phone(self, old_phone, new_phone):
        phone_obj = self.find_phone(old_phone)
        if phone_obj:
            phone_obj.value = Phone(new_phone).value

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]