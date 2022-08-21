myfile = open("poem.txt", 'r')
ch = ' '
vCount, cCount = 0
vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

while ch:
    ch = myfile.read(1)
    alphaCheck = ch.isalpha()
    if (ch in vowels) and alphaCheck :
        vCount += 1
    elif ch.isalph():
        cCount += 1

print("Vowels in file :", vCount)
print("Consonants in file :", cCount)