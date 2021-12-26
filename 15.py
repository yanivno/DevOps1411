whatToPrint = "hello world!"
listOfNames = ["michael","noam","lior","amichael"]
amountOfPrints = 4

for i in range(0,amountOfPrints):
    print(f"{i}){whatToPrint}")

for i in range(len(listOfNames)):
    print(listOfNames[i])

for name in listOfNames:
    print(name)


count = 1
while count < 101:
    if count % 7 == 0:
        print(f"{count} is a multiply of 7")
    if int(count / 10) == 7 or count % 10 == 7:  #i%7 ==0 or "7" in str(count)
        print(f"{count} has number 7")
    count += 1


a = 0
while a<10:
    print(a)
    a += 1;
else:
    print("completed successfully")