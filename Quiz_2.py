# Include two more questions about farming in your quiz.

def result():
    answer = ""
    for count in range(2):
        answer = input("Make your choice >>>>  ")
        if answer=="c":
            print('Correct!')
            break
        else:
            if count==1:
                print('The correct answer is c')
            else:
                print('Try again')
def quiz():
    print("Here is a quiz to test your knowledge of farming...")
    print()
    print("This week has a farming theme so we need to see what you know already about farms")
    print()
    print("Question 1")
    print("What percentage of land is used for farming? ")
    print()
    print("a.... 25%")
    print("b.... 50%")
    print("c.... 75%")
    print()
    result()
    print()
    print("Question 2")
    print("Which of these is not true? Wheat is used to make? ")
    print()
    print("a....plastic")
    print("b....bread")
    print("c....carpets")
    print()
    result()
    print()
    print("Question 2")
    print("Which of these crops is not grown by farmers in the UK? ")
    print()
    print("a.... hemp")
    print("b.... maize")
    print("c.... rice")
    print()
    result()
quiz()