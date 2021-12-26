# Q1 + Q2
try:
    a = 1/0
except ZeroDivisionError:
    print("cannot devide by zero")


# Q3
# the code is legal since except block is not mandatory in Python (STRANGE!!)
# if exception is thrown, code after finally block will not be executed.
try:
    x = 1
finally:
    print("finally")

# Q4 + Q5
# all exceptions are caught when using except statement without specifying the type - this is due to Inheritance.
# this is a very broad usage, and a bad practice. it can mask legitimate developer coding errors
# and cause all errors treated the same, as apposed to handling input errors and general coding errors differently.

# Q6
# IOError is thrown when using file handlers (including  console with print()) wrong way
# examples can be - writing to a closed file, handle is not valid (null), storage is full,etc.

# ZeroDivisionError is thrown when code is dividing by zero integer, usually in arithmetic operations

#Q7
print("Q7+Q8+Q9")
file_handle = open("words.txt","w")
file_handle.write("yaniv")
file_handle.close()

file_handle = open("words.txt","r")
for line in file_handle.readlines():
    print(line)
file_handle.close()

#Q11
print("Q11")
file_handle = open("hebtext.txt", "a+")
file_handle.write(input("write hebrew:")+"\n")
file_handle.flush()
file_handle.seek(0)
for line in file_handle.readlines():
    print(line,end='')
file_handle.close()


#Bonus
from PIL import Image, ImageDraw
blank_image = Image.new('RGBA', (400, 300), 'white')
img_draw = ImageDraw.Draw(blank_image)
img_draw.rectangle((70, 50, 270, 200), outline='red', fill='blue', width=4)
img_draw.text((70, 250), 'Hello World', fill='green')
blank_image.save('drawn_image.png')

