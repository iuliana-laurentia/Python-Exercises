#Extend the previous exercise so that it will display the string showing instances of the provided character and blank characters for the remaining letters. For example, if the string was "hello" and the user entered "l" the program would display " _ l l ".

targetStr = input("Please enter a string: ")
character = input("Please enter a character to find in the string: ")
found = False
for eachChar in targetStr:
    if eachChar == character:
        found = True
    else:
        found=False
        targetStr = targetStr.replace(eachChar, '_')
print(targetStr)
if not found:
    print("The character {0} is not in the string".format(character))


