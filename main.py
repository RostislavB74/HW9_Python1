# import pprint
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


@input_error
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


# input_error
def main():
    while True:
        # try:
        user_input = input(">>>")
        if user_input:
            command, data = parser(user_input)
            result = command(*data)
            if result:
                if result == "Good bye!":
                    print(result)
                    break
            print(result)
            # print("Unknown command\n Give me name and phone please")
        # except:
        #     continue


def no_command(*args):
    # print("Give me name and phone please")
    return "Unknown command\n Give me name and phone please"


def parser(text: str) -> tuple[callable, tuple[str] | None]:

    if text:
        text1 = text.lower()
        if text1.startswith("add"):
            return add, text.replace("add", "").strip().split()
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
    # res = []
    res = [print(f"Name contact: {key}  Phone number: {value}", end="\n") for key,
           value in address_book.items()]
    # for key,  value in address_book.items():

    # res.append(f"Name: {key}  Phone: number {value}")
    print(res)
    return
    # return ["{0}: {1}".format(key, value) for key, value in address_book.items()]
    # return [f"User: {key}  Phone: {value}" for key, value in address_book.items()]
    # list_data.append(k + ':' + str(v))


if __name__ == "__main__":
    main()
