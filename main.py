def add(*args):
    name = args[0]
    phone = args[1]
    return f"Add success {name} {phone}"


def no_command(*args):
    return "Unknown command"


def get_input(text: str):
    if text.startswith("hello"):
        return print("How can I help you?")
    if text.startswith("close"):
        return "Good bye!"


def parser(text: str) -> tuple[callable, tuple[str] | None]:
    if text.startswith("add"):
        return add, text.replace("add", "").strip().split()
    # if text.startswith("hello"):
    #     print("How can I help you?")
    #     return
    return no_command, None


def main():
    while True:
        user_input = input(">>>")
        command = get_input(user_input)
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
