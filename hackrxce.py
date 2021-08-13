from os import system, name
import itertools
import threading
import time
import sys
import datetime

from datetime import date

expirydate = datetime.date(2021, 9,10)
today=date.today()

if(expirydate>today):
    def chalo():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rhacking in the parity server for next colour--------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(30)
        done = True

    def chalo1():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rgetting the colour wait --------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(30)
        done = True

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    period=input("Enter your current period for price : ")
    period=int(period)
    clear()
    decision=1
    y=1
    banner='figlet RXCE'
    while(y):
        clear()
        system(banner)
        current=input("Enter Current Price :")
        chalo()
        print("\n---------Successfully hacked the server-----------")
        chalo1()
        print("\n---------Successfully got the colour -------------")
        print('\n')
        m=0
        def getSum(n):
            sum = 0
            for digit in str(n):
                sum += int(digit)
            return sum
        m=getSum(current)+1
        #print(m)
        newperiod=period+decision
        x=(newperiod,"GREEN","")
        y=(newperiod,"RED","")
        if(m%2==0):
            # print(period+decision)
            print(x)
        else:
            # print(period+decision)
            print(y)
        #input=input("")
        decision+=1
        y=input("Do you want to play : Press 1 and 0 to exit \n")

else:
    print("Your hack has expired--- Please contact on telegram -----------@Maneger399")
