from os import getenv
print("Hello World!")
name = getenv("NAME")
if (name == "yaniv"):
    print("you are ok")
else:
    print("I don't know who you are")