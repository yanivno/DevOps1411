try:
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))

    result = a/b
    print(result)
except ZeroDivisionError:
    print("could not divide by zero")
except BaseException as e:
    print("something went wrong: " + str(e.args))

def getUserAge():
    age = int(input("enter your age: "))
    if (age < 0):
        raise ValueError("age cannot be negative")