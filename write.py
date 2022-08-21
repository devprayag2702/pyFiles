

myfile = open("Student1.txt", 'w')

for i in range(5):
    name = input("Enter name of student : ")
    myfile.write(name)
    myfile.write('\n')

myfile.close()