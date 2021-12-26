from one import addition
from two import get_input_from_user


def main():
    a = get_input_from_user()
    b = get_input_from_user()
    result = addition(a, b)
    print(result)


main()