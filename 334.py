#myFile = open("read_my_contents.txt")
#for line in myFile.readlines():
#    print(line.strip("\n"))

#myOtherFile = open("moshe.txt","w")
#myOtherFile.write("hey hey\n")

with open("names.txt") as f:
    for line in f.readlines():
        print(line)

def writeName(name,fileName):
    handle = open(fileName,"a")
    handle.write(name+"\n")
    handle.close()

def readNames(fileName):
    handle = open(fileName,"r")
    for line in handle.readlines():
        print("hello " + line.strip("\n"))
    handle.close()

writeName(input("write name:"),"names.txt")
readNames("names.txt")