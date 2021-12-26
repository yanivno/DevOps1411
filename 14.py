isTrue = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"

if a >= 2 and strOne == "One":
    print("a is greater than 2")
elif b==2:
    print("something")
else:
    print("a is lower than 2")

my_list = ["hen","lior","shay","ariel"]
if "hen" in my_list:
    print("we found hen")

my_other_list = []
if my_other_list:
    print("not empty list")

if len(my_other_list) > 0:
    print("not empty list")

c = 5
d = 5
if c is d:
    print("c is d")

a = ["ee", "dd"]
b = ["dd", "ee"]
if a == b:
    print("comparison")

e = 9
if type(e) is int :
    print("e is int")