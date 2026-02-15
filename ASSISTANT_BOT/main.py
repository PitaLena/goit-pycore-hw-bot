from src.parser import parse_input
from src.handlers import add_contact, change_contact, show_phone, show_all


def main() -> None:
    contacts: dict[str, str] = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command == "":
            print("Invalid command.")
            continue

        if command == "hello":
            print("How can I help you?")

        elif command == "add":
            if len(args) != 2:
                print("Invalid command.")
            else:
                print(add_contact(args, contacts))

        elif command == "change":
            if len(args) != 2:
                print("Invalid command.")
            else:
                print(change_contact(args, contacts))

        elif command == "phone":
            if len(args) != 1:
                print("Invalid command.")
            else:
                print(show_phone(args, contacts))

        elif command == "all":
            if args:
                print("Invalid command.")
            else:
                print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
