#Extend the previous exercise to convert the binary number to hexadecimal.
#Create a program to convert from hexadecimal to decimal.

def main():
    number = int(input('Input a number up to 255:'))
    if number > 0 and number <226:
        number=hex(number)
        print(number)
    else:
        print('This number is out of range! ')
    number=int(number, 16)
    print(number)

main()