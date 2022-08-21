
count = int(input("How many students are there in the class?"))
myfile = open("Student1.txt", 'w')

for i in range(count):
    print("Enter details for student", (i+1), "below:")
    rollno = int(input("Rollno : "))
    name = input("Name : ")
    marks = float(input("Marks : "))
    record = str(rollno) + ',' + name + ',' + str(marks) + '\n'
    myfile.write(name)

myfile.close()
