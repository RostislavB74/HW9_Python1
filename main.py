def add(*args):
    name = args[0]
    phone = args[1]
    return f"Add success {name} {phone}"


def no_command(*args):
    return "Unknown command"


def get_input(text: str) -> tuple[callable, tuple[str] | None]:
    text_lower = text.lower()
    if text_lower.startswith("hello"):
        return "How can I help you?"
    if text_lower.startswith("close") or text_lower.startswith("exit") or text_lower.startswith("good bye"):
        return "Good bye!"
    if text_lower.startswith("add"):
        # new_contact = []
        # contact_book = (text.replace("add", "").strip().split())
        # print(add, text.replace("add", "").strip().split())
        # print(contact_book)
        return add, text.replace("add", "").strip().split()
        # print(type(contact_book))
        # return contact_book
    # if text_lower.startswith("show all"):
     #   contact_book:
      #      print(contact_book)
    return no_command, None


def main():
    while True:
        user_input = input(">>>")
        command = get_input(user_input)
        print(command)
        # command, data = parser(user_input)
        if command == "Good bye!":
            print(command)
            break
        # print(command)


if __name__ == "__main__":
    main()
# @format_phone_number
# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#             .removeprefix("+")
#             .replace("(", "")
#             .replace(")", "")
#             .replace("-", "")
#             .replace(" ", "")
#     )
#     return new_phone
