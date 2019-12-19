#Create a program which will count down from 10 to 0, indicating how long there is to go before time runs outs. When time runs out it should display a suitable message.

import time
def main():
    for timeCount in range(10,0,-1):
        print("{0:>2} seconds remaining!".format(timeCount))
        time.sleep(1)
    print("YOUR TIME IS UP!!!!!")

main()