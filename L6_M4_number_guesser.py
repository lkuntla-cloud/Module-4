import random
import time
number=random.randint(1,100)
def intro():
    print("Hello User what is your name?")
    global name
    name=input()
    print("Hello ",name," welcome to the game of guessing a number between 1 and 100")
    if number%2==0:
        x="even"
    if number%2!=0:
        x="odd"
    print("The number you have to guess is ",x)
    time.sleep(.5)
    print("go ahead and guess!")
def pik():
    gt=0
    while gt<=6:
        try:
            time.sleep(.25)
            guess=int(input())
            
            if guess <100 or guess>1:
                gt=gt+1
                if gt<=6:
                    if guess>number:
                        print("Your guess is greater than the number")
                    if guess<number:
                        print("Your guess is smaller than the number")
                    if guess!=number:
                        print("Your guess is not equal to the number try again")
                        time.sleep(.5)
                    if guess==number:
                        break
            if guess>100 or guess<1:
                print("You input is not in the given range")
                time.sleep(.25)
        except:
            print("I don't think that {} is a number sorry".format(guess))
    if guess==number:
        gt=str(gt)
        print("well done {} you have guessed the number it was {}".format(name,number))
    if guess!=number:
        print("No that was not the number I was thinking of the answer was "+str(number))
playagain="yes"
while playagain=="yes"or playagain=="y" or playagain=="Yes":
    intro()
    pik()
    print("Do you want to play again?")
    playagain=input()