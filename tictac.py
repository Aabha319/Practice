import sys
t=[1,2,3,4,5,6,7,8,9]
user=""
combo1 = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
def check(user):
    if (t[0]== user and t[1]==user and t[2]== user) or (t[3]== user and t[4]==user and t[5]== user) or (t[6]== user and t[7]==user and t[8]== user) :
        print(f"{user} won")
        sys.exit()
    elif (t[0]== user and t[3]==user and t[6]== user) or (t[1]== user and t[4]==user and t[7]== user) or (t[2]== user and t[5]==user and t[8]== user) :
        print(f"{user} won")
        sys.exit()
    elif (t[0]== user and t[4]==user and t[8]== user) or (t[2]== user and t[4]==user and t[6]== user) :
        print(f"{user} won")
        sys.exit()

def display(pos1,user):
        t[pos1-1]=user
        print(f"\t{t[0]}\t|\t{t[1]}\t|\t{t[2]}\t")
        print(f"----------------------------")
        print(f"\t{t[3]}\t|\t{t[4]}\t|\t{t[5]}\t")
        print(f"----------------------------")
        print(f"\t{t[6]}\t|\t{t[7]}\t|\t{t[8]}\t")
user1='X'
user2='0'
pos = [1,2,3,4,5,6,7,8,9]
global pos1
def play(user):
    pos1 = int(input(f"Which position do you wish to play, available position is {pos}"))
    if(pos1 in pos ):
        pos.remove(pos1)
        display(pos1,user)
    else:
        print("used position please retry")
cnt=1
display(1,"1")
while(cnt<=5):
    play(user1)
    check(user1)
    if(cnt == 5):
        break
    play(user2)
    check(user2)
    cnt=cnt+1