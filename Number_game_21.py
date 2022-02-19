import random
def check(turn,n):
    for i in turn:
        if(i==n):
            return False
    return True
def lose():
    print("You Lose the Game try again later!")
def start():
    num=0
    turn=[0]
    print("Press 1 for Your Chance first")
    print("Press 2 for Computer chance first")
    userChoice=input("Enter")
    if userChoice=='1':
        while(num<=21):
            if userChoice=='1':
                print("Your Turn")
                print(turn[1:])
                many=int(input("Enter How many number you want to enter High(3):"))
                if many>3:
                    print("Please Follow the Instructions! Try Again Next time")
                    lose() 
                    return
                else:
                    for i in range(many):
                        n=int(input("Enter the Number in ascending Order:"))
                        if(check(turn,n)!=True or n==21):
                            lose()
                            return
                        turn.append(n)
            if(userChoice=='1'):
                for i in range(random.randint(1,3)):
                    if(turn[-1]==20):
                        print("You Win!")
                        return
                    turn.append(turn[-1]+1)


    elif userChoice=='2':
        while(num<=21):
            if(userChoice=='2'):
                for i in range(random.randint(1,3)):
                    turn.append(turn[-1]+1)
                    if(turn[-1]>=20):
                        print("You Win!")
                        return
            if userChoice=='2':
                print("Your Turn")
                print(turn[1:])
                many=int(input("Enter How many number you want to enter High(3):"))
                if many>3:
                    print("Please Follow the Instructions! Try Again Next time")
                    lose() 
                    return
                else:
                    for i in range(many):
                        n=int(input("Enter the Number in ascending Order:"))
                        if(check(turn,n)!=True or n==21):
                            lose()
                            return
                        turn.append(n)
    else:
        print("Enter Legal Value")
        return


choice=True
while choice==True:
    print("Welcome to 21 number Game")
    res=input("Do you want to play the Game Yes/No: ")
    if res=='Yes':
        start()
    elif res=='No':
        print("Bye Bye👋👋👋")
        choice=False
    else:
        print("Please Enter the legal value!👆👆")