import random
user1=(input("Enter the name of the first player"))
user2=(input("Enter the name of the second player"))
sum1=0
sum2=0
s=[17,21,30,43,55,61,73,99]
l=[6,14,32,50,68,70,82,88]
while sum1!=100 and sum2!=100 :
    ch1=(input(user1+" Press y to roll the dice?"))
    if ch1=='y':
        x=random.randint(1,6)
        print("Your roll dice is",x)
        sum1=sum1+x
            if sum1<100:
                a=random.randint(5,17)
                if sum1 in s :
                    print("Oops a snake bite:(")
                    sum1=sum1-a
                if sum1 in l :
                    print("Congratulations :)")
                    sum1=sum1+a
        print("Your current position is",sum1)
        if sum1>=100:
            print(user1+" has won")
    ch2=(input(user2+" Do you wish to roll the dice?"))
    print("Press y to continue")
    if ch2=='y':
        x=random.randint(1, 6)
        print("Your roll dice is",x)
            sum2=sum2+x
            # if sum2<100:
                a = random.randint(5,17)
                if sum2 in s :
                    print("Oops a snake bite:(")
                    sum2=sum2-a
               
                if sum2 in l :
                    print("Congratulations :)")
                    sum2=sum2+a
        print("Your current total is",sum2)
        if sum2>=100:
            print(user2+" has won")


