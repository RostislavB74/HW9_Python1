import functools

address_book = {}


# def input_error(func):
#     #     #        @functools.wraps(func)
#     def inner(*args, **kwargs):

#         try:
#             func(*args, **kwargs)
#         except IndexError:
#             print("Please input : \" add name phone\"")
#             return func(*args, **kwargs)
#         except TypeError:
#             print("Give me name and phone please")
#             return func(*args, **kwargs)
#     return inner

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


# def input_error(func):
#     # @functools.wraps(func)
#     def inner(*args, **kwargs):

#         try:
#             func(*args, **kwargs)
#         except:


#     return inner
# @input_error
# @retry(max_tries=10)


def add(*args):
    name = args[0]
    phone = args[1]
    address_book[name] = phone
    # print(contact)
    return f"Add success {name} {phone}"

# @input_error
# @retry(max_tries=10)


def change(*args):
    name = args[0]
    phone = args[1]
    address_book[name] = phone
    # print(contact)
    return f"Change success {name} {phone}"

# @input_error
# @retry(max_tries=10)


def exit(*args):
    return "Good bye!"

# @input_error
# @retry(max_tries=10)


def get_phone(*args):
    name = args[0]
    return f"User:{name}  Phone: {address_book[name]}"

# @input_error
# @retry(max_tries=10)


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

# @input_error
# @retry(max_tries=10)


def no_command(*args, **kwargs):
    return "Unknown command"


# @input_error
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
    return [f"Phone: {key}  User: {value}" for key, value in address_book.items()]


if __name__ == "__main__":
    main()
