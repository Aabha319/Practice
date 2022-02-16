board=[0,1,2,3,4,5,6,7,8]

def show():
    print("-----------")
    print(f"|",board[0],"|",board[1],"|",board[2])
    print("-----------")
    print(f"|",board[3],"|",board[4],"|",board[5])
    print("-----------")
    print(f"|", board[6],"|",board[7],"|", board[8])
    print("-----------")


user1=(input(" enter the name of the first player "))
user2=(input(" enter the name of the second player "))
show()


def checkline(ch, s1, s2, s3):
    if board[s1] == ch and board[s2] == ch and board[s3] == ch:
        return True


def check(ch):
    if checkline(ch, 0, 1, 2):
        return True
    if checkline(ch, 3, 4, 5):
        return True
    if checkline(ch, 6, 7, 8):
        return True
    if checkline(ch, 0, 3, 6):
        return True
    if checkline(ch, 1, 4, 7):
        return True
    if checkline(ch, 2, 5, 8):
        return True
    if checkline(ch, 0, 4, 8):
        return True
    if checkline(ch, 2, 4, 6):
        return True


while True:
    u1=int(input(f"{user1} enter the position"))
    if board[u1]!='X' and board[u1]!='O':
        board[u1]='X'
        show()
        if check("X")== True:
            print(user1+"is the winner")
            break
    while True:
        u2 = int(input(f"{user2} enter the position"))
        if board[u2] != 'X' and board[u2] != 'O':
            board[u2] = 'O'
            show()
            if check("O") == True:
                print(user1 + "is the winner")
            break

