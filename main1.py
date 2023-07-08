address_book = {}


def add(*args):

    name = args[0]
    phone = args[1]
    address_book[name] = phone
    # print(contact)
    return f"Add success {name} {phone}"


def change(*args):
    name = args[0]
    phone = args[1]
    address_book[name] = phone
    # print(contact)
    return f"Change success {name} {phone}"


def show_all(*args):
    return [f"Phone: {key}  User: {value}" for key, value in address_book.items()]


def get_phone(*args):
    name = args[0]
    return f"User:{name}  Phone: {address_book[name]}"
    # list ( map(lambda i: i.get('email'), users) )


def no_command(*args):
    return "Unknown command"


def hello(*args):
    return "How can I help you?"


def exit(*args):
    return "Good bye!"


def parser(text: str) -> tuple[callable, tuple[str] | None]:
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
        return get_phone, text.replace("change", "").strip().split()
    return no_command, None


def main():
    while True:
        user_input = input(">>>")
        command, data = parser(user_input)
        result = command(*data)
        if result == "Good bye!":
            print(result)
            break

        print(result)


if __name__ == "__main__":
    main()
# def add(*args):
#     name = Name(args[0])
#     phone = Phone(args[1])
#     rec = Record(name, phone)
#     return addressbook.add_rec(rec)
