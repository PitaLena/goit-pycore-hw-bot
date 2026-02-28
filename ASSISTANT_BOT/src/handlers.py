from src.decorators import input_error
from src.address_book import Record


@input_error
def add_contact(args, book):
    name, phone, *_ = args
    record = book.find(name)

    if record is None:
        record = Record(name)
        book.add_record(record)
        record.add_phone(phone)
        return "Contact added."

    record.add_phone(phone)
    return "Contact updated."


@input_error
def change_contact(args, book):
    name, old_phone, new_phone = args
    record = book.find(name)
    if not record:
        raise ValueError("Contact not found")

    record.edit_phone(old_phone, new_phone)
    return "Phone updated."


@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if not record:
        raise ValueError("Contact not found")

    phones = "; ".join(p.value for p in record.phones)
    return phones


@input_error
def show_all(args, book):
    if not book.data:
        return "Address book is empty."
    return "\n".join(str(record) for record in book.data.values())


@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if not record:
        raise ValueError("Contact not found")

    record.add_birthday(birthday)
    return "Birthday added."

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if not record:
        raise ValueError("Contact not found")

    if not record.birthday:
        return "Birthday not set."

    return str(record.birthday)

@input_error
def birthdays(args, book):
    upcoming = book.get_upcoming_birthdays()

    if not upcoming:
        return "No upcoming birthdays."

    result = []
    for item in upcoming:
        result.append(f"{item['name']} - {item['congratulation_date']}")

    return "\n".join(result)