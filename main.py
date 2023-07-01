

def add(*args):
    name = args[0]
    phone = args[1]
    return f"Add success {name} {phone}"


def no_command(*args):
    return "Unknown command"


def parser(text: str) -> tuple[callable, tuple[str] | None]:
    if text.startswith("add"):
        return add, text.replace("add", "").strip().split()
    return no_command, None


def main():
    while True:
        user_input = input(">>>")
        if user_input == 'hello':
            print('Hello')
        command, data = parser(user_input)
        result = command(*data)
        print(result)


if __name__ == '__main__':
    main()
