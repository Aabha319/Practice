import time
flag1=False
flag2=False
hint="yes"
p1 = input("enter your name")
p2 = input("enter your name")
combo = "GONE"
print(f"{p1} and {p2} Make a word from N O E G")
cnt = 1
count = 0
start = time.time()
while(cnt <= 3):
    if count == 0:
        hint = input(f"You wish to use hint? {p1}")
    if (hint == "yes" and count == 0):
        print("Your word start with G and ends with E")
        count = 1
    a1 = input(f"Enter your ans:{p1}\n Chance no {cnt}")

    cnt = cnt + 1
    if(a1 == combo):
        break
end = time.time()
t1=end-start
if(a1==combo):
    flag1 = True
if(count == 1):
    t1=t1+5
cnt = 1
count = 0
hint="yes"
start = time.time()
while(cnt <= 3):
    if count == 0:
        hint = input(f"You wish to use hint? {p2}")
    if (hint == "yes" and count == 0):
        count = 1
        print("Your word start with G and ends with E")
    a2 = input(f"Enter your ans:{p2}\n Chance no {cnt}")
    cnt = cnt + 1

    if(a2 == combo):
        break
end = time.time()
t2=end-start
if(count == 1):
    t2=t2+5
if(a2==combo):
    flag2 = True
if(t1<t2 and flag1 == True):
    print("player 1 won")
elif(t2<t1 and flag2 == True):
    print("player 2 won")
elif(t2==t1 and flag1 == True and flag2 == True):
    print("there is a tie")
elif(t2==t1 and flag1 == False and flag2 == True):
    print("player 1 won")
elif(t2==t1 and flag1 == True and flag2 == False):
    print("player 2 won")
else:
    print("No 1 Won")

