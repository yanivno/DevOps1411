#Q. A
print("EX. A")
X = 5
Y = 3
if (X > Y):
    print("BIG")
else:
    print("small")


#Q.B
print("EX. B")
for i in range(1,6):
    print("iteration " + str(i))

#Q C
print("EX. C")
variable = 3
if (variable == 1):
    print("summer")
elif (variable == 2):
    print("winter")
elif(variable == 3):
    print("fall")
elif(variable == 4):
    print("spring")
else:
    print("not a number between 1-4")

#Q 4
print("EX D")
#the loop will run 10 times - 1-10(including)
#last thing printed is 10.

#Q 5
print ("EX E")
age = 34
firstLetterName = "Y"
currUsdExchangeRate = 3.11
didIFlyAbroad = True
aptNumber = 11
print ("age: "+str(age))
print("first letter of name: " + firstLetterName)
print("current USD/NIS Exchange Rate: " + str(currUsdExchangeRate))
print("Did I Flew abroard: " + str(didIFlyAbroad))
print("Apartment Number: " + str(aptNumber))
if ((age + currUsdExchangeRate) > 30):
    print("result is larger than 30")
else:
    print("result is smaller than 30")


#Q 6
print("EX F")
phoneNumber = input("enter phone number: ")
print("Phone Number: " + phoneNumber)

#Q7
print("EX G")
def printHello():
    print("Hello")

def calculate():
    number = 5 + 3.2
    print(number)

printHello()
calculate()

#Q8
print("EX H")
def printName(name):
    print("your name is : " + str(name))
def divider(num):
    print("orig number: " + str(num))
    print("divided result : " + str(num/2))


printName(input("enter your name:"))
divider(44)

#Q9
print("EX I")
def summer(num1,num2):
    return num1 + num2

def concater(str1,str2):
    return str1 + " " + str2

print(summer(33,32))
print(concater("yaniv", "is my hero"))

#Q10
print("EX K")
for i in range(1,6):
    line = ""
    for j in range(0,i):
        line += "*"
    print(line)

#Q11
print("EX L")
size = 7
for i in range(0, size):
    line = [" "] * size
    for j in range(0, size):
        if ((i == j) or (j+i == size - 1)):
            line[j] = "*"
        else:
            line[j] = " "
    print("".join(line))

#Q12
print("EX M")

def getNum():
    isNum = False
    while (not isNum):
        num = input("enter Number: ")
        isNum = num.isnumeric()
    return num

def sumOfDigits(strNum):
    sum = 0
    for i in range(0,len(strNum)):
        sum += int(strNum[i])
    return sum

print(sumOfDigits(getNum()))
