def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2:
        return "Invalid command."

    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2:
        return "Invalid command."

    name, phone = args

    if name not in contacts:
        return "Contact not found."

    contacts[name] = phone
    return "Contact updated."


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 1:
        return "Invalid command."

    name = args[0]

    if name not in contacts:
        return "Contact not found."

    return contacts[name]


def show_all(contacts: dict[str, str]) -> str:
    if not contacts:
        return "No contacts saved."

    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())