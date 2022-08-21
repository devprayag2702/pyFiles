
myfile = open("poem.txt", 'r')           # opening the file in read mode

print("Reading first 30 bytes : ")
str1 = myfile.read(30)                    # here, the read function is reading 30 bytes
print(str1)

print("Reading next 9 bytes : ")
str2 = myfile.read(9)
print(str2)

print("Reading a line : ")
str3 = myfile.readline()
print(str3)

print("Reading the remaining file : ")
str4 = myfile.read()
print(str4)
