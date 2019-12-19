#Write a program that will add together a series of numbers until the user enters a rogue value of 0. The program will then display the total.

def main():
    n=''
    sum = 0
    while True:
        n = int(input('Please type a number:'))
        if n != 0:
            sum=sum+n
        else:
            print('The sum of the numbers given is', sum)
            break

main()