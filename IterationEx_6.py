#Create a program which will convert a given decimal up to 255 into its 8-bit binary equivalent.

def main():
    number = int(input('Input a number up to 255:'))
    if number > 0 and number <226:
        number=bin(number)
        print(number)
    else:
        print('This number is out of range! ')

main()