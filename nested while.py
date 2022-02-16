"""i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) :
       print (i, " is prime")
   i = i + 1

print ("Good bye!")"""
import time
user1=input("enter name USER 1")
cnt1=0
cnt2=0
cnt3=0
print(user1+" word for you is C_M_U_T_R")
while cnt1<3:
        guess=input("enter ur choice")
        if guess=="COMPUTER":
            print("correct answer")
            break
        else:
          print("Try again")
          cnt1=cnt1+1
        if cnt1==4:
            print("play again")
            break
        
while (guess=="COMPUTER"):
    while(cnt2<3):
        print(user1+" word for you is S_F_W_R_")
        guess=input("enter ur choice")
        if guess=="SOFTWARE":
            print("correct answer")
            break
        else:
            print("Try again")
            cnt2=cnt2+1
        if cnt2==4:
            print("play again")
            break
        
while (guess=="SOFTWARE"):
    while(cnt3<3):
        print(user1+" word for you is P_T__N")
        guess=input("enter ur choice")
        if guess=="PYTHON":
            print("correct answer")
            break
        else:
            print("Try again")
            cnt3=cnt3+1
        if cnt3==4:
            print("play again")
            break
    
    
