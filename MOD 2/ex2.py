myString = "habjwabfjahf"
reversedString = ''

for i in range(len(myString)-1,-1,-1):
    print(myString[i])
    reversedString+=myString[i]

print(reversedString)