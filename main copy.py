address_book = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            print("Give me name and phone please")
        except TypeError:
            print("Give me name and phone please")
        except ValueError:
            print("Give me name and phone please")
    return wrapper


@input_error
def add(*args):
    name = str.capitalize(args[0])
    phone = args[1]
    address_book[str.capitalize(name)] = phone
    return f"Add success {name} {phone}"


@input_error
def change(*args):
    name = str.capitalize(args[0])
    phone = args[1]
    address_book[str.capitalize(name)] = phone
    return f"Change success {str.capitalize(name)} {phone}"


def exit(*args):
    return "Good bye!"


@input_error
def get_phone(*args):
    name = str.capitalize(args[0])
    return f"User:{name}  Phone: {address_book[name]}"


def hello(*args):
    return "How can I help you?"


# @input_error
def main():
    while True:
        user_input = input(">>>")
        if user_input:
            command, data = parser(user_input)
            result = command(*data)
            if result:
                if result == "Good bye!":
                    print(result)
                    break
                print(result)
            continue
        else:
            print(no_command())


def no_command(*args, **kwargs):
    return "Unknown command"


def parser(text: str) -> tuple[callable, tuple[str] | None]:

    if text:
        text1 = text.lower()
        if text1.startswith("add"):
            return add, text1.replace("add", "").strip().split()
        if text1.startswith("hello"):
            return hello, "How can I help you?"
        if text1.startswith("close") or text1.startswith("exit") or text1.startswith("good bye"):
            return exit, "Good bye!"
        if text1.startswith("show all"):
            return show_all, 'show all'
        if text1.startswith("phone"):
            return get_phone, text.replace("phone", "").strip().split()
        if text1.startswith("change"):
            return change, text.replace("change", "").strip().split()
        else:
            return no_command, ''
    else:
        return no_command, ''


def show_all(*args):

    [print(f"Name contact: {key}  Phone number: {value}", end="\n") for key,
     value in address_book.items()]
    return


if __name__ == "__main__":
    main()
