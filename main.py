address_book = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        count = 10

        while count:
            try:
                return func(*args, **kwargs)
            except IndexError:
                count -= 1
                print("Please input : \" add name phone\"")
                print(f"{count} tries left")
            except TypeError:
                count -= 1
                print("Give me name and phone please")
                print(f"{count} tries left")
            except ValueError:
                count -= 1
                print("Please input : \" add name phone\"")
                print(f"{count} tries left")

    return wrapper


def add(*args):
    name = args[0]
    phone = args[1]
    address_book[name] = phone
    return f"Add success {name} {phone}"


def change(*args):
    name = args[0]
    phone = args[1]
    address_book[name] = phone
    return f"Change success {name} {phone}"


def exit(*args):
    return "Good bye!"


def get_phone(*args):
    name = args[0]
    return f"User:{name}  Phone: {address_book[name]}"


def hello(*args):
    return "How can I help you?"


@input_error
def main():
    while True:
        # try:
        user_input = input(">>>")
        if user_input:
            command, data = parser(user_input)
            result = command(*data)
            if result == "Good bye!":
                print(result)
                break
            print(result)
        else:
            print(no_command())
            # except:
        #     continue


def no_command(*args, **kwargs):
    return "Unknown command"


def parser(text: str) -> tuple[callable, tuple[str] | None]:

    if text:
        text = text.lower()
        if text.startswith("add"):
            return add, text.replace("add", "").strip().split()
        if text.startswith("hello"):
            return hello, "How can I help you?"
        if text.startswith("close") or text.startswith("exit") or text.startswith("good bye"):
            return exit, "Good bye!"
        if text.startswith("show all"):
            return show_all, 'show all'
        if text.startswith("phone"):
            return get_phone, text.replace("phone", "").strip().split()
        if text.startswith("change"):
            return change, text.replace("change", "").strip().split()
    else:
        return no_command, None


def show_all(*args):
    return [f"User: {key}  Phone: {value}" for key, value in address_book.items()]


if __name__ == "__main__":
    main()
