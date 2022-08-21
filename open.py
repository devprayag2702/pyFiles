
myfile = open("poem.txt", 'r')           # opening the file in read mode

str1 = myfile.read(30)                    # here, the read function is reading 30 bytes

print(str1)

str2 = myfile.read(9)

print(str2)

str3 = myfile.readline()

print(str3)

str4 = myfile.read()

print(str4)