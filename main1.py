def add(*args):
    name = args[0]
    phone = args[1]
    return f"Add success {name} {phone}"


def no_command(*args):
    return "Unknown command"


def parser(text: str) -> tuple[callable, tuple[str] | None]:
    # text_lower = text.lower()
    if text.startswith("add"):
        return add, text.replace("add", "").strip().split()
    # if text_lower.startswith("hello"):
   #     return "How can I help you?"
    if text_lower.startswith("close") or text_lower.startswith("exit") or text_lower.startswith("good bye"):
        return "Good bye!"
    return no_command, None


def main():
    while True:
        user_input = input(">>>")
        command, data = parser(user_input)
        result = command(*data)
        print(result)


if __name__ == "__main__":
    main()
