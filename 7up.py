import random
import time
p1=input("name")
a1=1000
x=["up","down","7"]
while a1>0:
    amt1=int(input("enter amount for bet"))
    choose=input("do u wish to play")
    if choose=="yes":
        bet=input("Enter the option on which you want to bet:- up, down, 7?")
        print("Great!! you are betting on "+bet);
        print("Get ready!! We are tossing the coin!!")
        time.sleep(2)
        choice=random.choice(x)
        print("The option selected= "+choice)
        if choice==bet:
            print("Yay!! congrats, you win the bet")
            a1=a1+amt1
            print("Your current amount after winning =",a1)
        else:
            print("Oopss! sorry, you lost the bet")
            a1=a1-amt1
            print("Your current amount after losing =",a1)
if a1<=0:
    print("Sorry!! Your play Limit is over")
        
    
    
    
    
    
