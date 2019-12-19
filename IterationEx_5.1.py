#Create a program that uses linear search to check that a given character is in a given string.

def linear_search(string, s):
    for i in range(len(string)):
        if string[i]==s:
            return i
    return -1

string=str(input('write a word:'))
string=list(string)
s=str(input('enter searching element:'))

result=linear_search(string, s)
if result==-1:
    print('Character NOT found')
else:
    string=str(string)
    print(string.replace('a', '|'))
