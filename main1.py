def add(*args):
    contact = {}
    name = args[0]
    phone = args[1]
    contact[phone] = name
    return f"Add success {name} {phone}"


def address_book(contact):
    contact = {}
    address_book = []
    address_book.append(contact)
    return address_book


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
        return address_book
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
