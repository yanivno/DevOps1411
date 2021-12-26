print("hello")
my_var = 10
print(my_var)
my_name = "Yaniv"
print(my_name)
is_true = False
my_list = ["Yaniv", "Norman", 34, True];
print(my_list[1])

my_dict = {"name":"Yaniv", "lname": "Norman", "age": 34, "is_married": False}
print(my_dict["name"])
print(my_dict.keys())
my_number = 5*2
my_other = 5 * "Yaniv"
print(my_other)

if my_number == 10:
    print("my_number")

fname = "Yaniv"
lname = "Norman"
print("Hello " + fname + " " + lname)
print(f"Hello {fname} {lname}")
print("Hello %s %s" % (fname,lname))

#Last
my_number = "4"
result = int(my_number) - 2
print(result)
print("your result is " + str(result))
my_list = [1,2,3,4]
print(f"your result is {my_list[0::2]}")
my_str = "hello and welcome \\\" all all all \\\""
my_dict = {"fname":"Yaniv","lname":"Norman","age":34,"id":123456789}
key_to_print = input(f"enter key: {list(my_dict.keys())}")
print("you chose to print: " + str(my_dict[key_to_print]));
