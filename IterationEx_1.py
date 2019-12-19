#Create a program that will ask the user for a number and then print out a list of number from 1 to the number entered and the square of the number.

def main():
    number=int(input('Please type a number:'))
    for n in range(number+1):
        squared_value=n**2
        print("{0} squared is {1} points.".format(n, squared_value))

main()