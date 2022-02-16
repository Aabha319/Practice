import sys
cnt = 1
sum = 0

def lifel(qt):
    ll = input(f"Which lifeline you wish to use, options available are {lifeline}")
    if(ll == "fiftyfifty"):
        lifeline.remove(ll)
        if(qt==1):
            del q[1]['C']
            del q[1]['D']
        elif (qt == 2):
            del q[2]['C']
            del q[2]['B']
        elif (qt == 3):
            del q[3]['A']
            del q[3]['B']
        elif (qt == 4):
            del q[4]['A']
            del q[4]['D']
        elif (qt == 5):
            del q[5]['D']
            del q[5]['B']
        elif (qt == 6):
            del q[6]['D']
            del q[6]['B']
    elif(ll == "audience poll"):
        lifeline.remove(ll)
        if (qt == 1):
            print("A ---- 20%\nB ---- 60%\nC ---- 10%\nD ----10%")
        elif (qt == 2):
            print("A ---- 10%\nB ---- 10%\nC ---- 10%\nD ----70%")
        elif (qt == 3):
            print("A ---- 20%\nB ---- 20%\nC ---- 50%\nD ----10%")
        elif (qt == 4):
            print("A ---- 20%\nB ---- 20%\nC ---- 50%\nD ----10%")
        elif (qt == 5):
            print("A ---- 20%\nB ---- 20%\nC ---- 50%\nD ----10%")
        elif (qt == 6):
            print("A ---- 20%\nB ---- 20%\nC ---- 50%\nD ----10%")
    else:
        return

def check(a,level):
    global cnt,sum
    amt = 0
    print(sum)
    if(q[cnt][a] in ans and cnt < 6  ):
        amt = 1000 * cnt
        sum = sum + amt
        cnt = cnt+1
        print(f"Congratulations you have won Rs {amt}, so the total is {sum}")
    else:
        if(level == 1):
            print("you won Rs. 0, Better luck next time")
        elif(level == 2):
            print("you won Rs 3000, Better luck next time")
        elif(level == 3 and sum == 15000):
            print("you won Rs 10000,Better luck next time")
        sys.exit();


print("Welcome to the Game of KBC.")
name=input("Enter your name")
ans=['peacock', 'hockey','tiger', 'Narendra Modi', 'Aaryabhatta', 'Steve Jobs']
q={1:{'A':'pigeon', 'B':'peacock', 'C':'hen', 'D':'ostrich'},
   2:{'A':'soccer', 'B':'football', 'C':'cricket', 'D':'hockey'},
   3:{'A':'lion', 'B':'elephant', 'C':'tiger', 'D':'fox'},
   4:{'A':'Rahul Gandhi', 'B':'Manmohan Singh', 'C':'Narendra Modi', 'D':'Jawarlal Nehru'},
   5:{'A':'Newton', 'B':'Dalton', 'C':'Aaryabhatta', 'D':'Lavsoviour'},
   6:{'A':'Sundar Pichai', 'B':'Ambani', 'C':'Steve Jobs', 'D':'Mark'}}

lifeline = ['fiftyfifty','audience poll']
flag = True
while(flag == True):
    print ("Name the national bird")
    lifel(1)
    a = input(q[1])
    check(a,1)
    print("Name the national game")
    lifel(2)
    a = input(q[2])
    check(a,1)
    print("you have cleared level 1")
    print ("Name the national animal")
    lifel(3)
    a = input(q[3])
    check(a,2)
    print ("Name the prime minister of india")
    lifel(4)
    a = input(q[4])
    check(a,2)
    print("you have cleared level 2")
    print ("Who has invented Zero?")
    lifel(5)
    a = input(q[5])
    check(a,3)
    print ("Who is the founder of Apple?")
    lifel(6)
    a = input(q[6])
    check(a,3)
    print("congratulations you won Rs 6000")