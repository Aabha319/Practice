

import time
user1=input("enter name USER 1")
user2=input("enter name USER 2")
z=0;t=0;cnt1=0;cnt2=0
print(user1+" word for you is C_M_U_T_R")
while cnt1<3:
        z1=time.time()
        guess=input()
        
        if guess=="COMPUTER":
          z2=time.time()
          z=z2-z1
          print(z)
          cnt1=1
          break
        else:
          print("Try again")
          cnt1=cnt1+1
print(user2+" word for you is S_F_W_R_")
while cnt2<3:
  t1=time.time()
  guess=input()
  if guess=="SOFTWARE":
    t2=time.time()
    t=t2-t1
    print(t)
    cnt2=1
    break
  else:
    print("Try again")
    cnt2=cnt2+1
  
if cnt1==1 and cnt2==1:  
    if z>t:
      print("user2 win")
    else:
      print("user1 wins")
if cnt1==1 and cnt2!=1:
  print("user1 win")
if cnt2==1 and cnt1!=1:
  print("user2 wins")
if cnt1>=3:
  print("attempt over for user1")
if cnt2>=3: 
  print("attempt over for user2")
