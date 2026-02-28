def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except IndexError:
            return "Enter the argument for the command"

        except ValueError as e:
            if "unpack" in str(e):
                return "Give me name and phone please."           
            return str(e)

        except KeyError:
            return "Contact not found."

    return inner