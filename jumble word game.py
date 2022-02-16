import random
import time
l1=["flower","maths","python","laptop","game","chocolate","trees"]
word=random.choice(l1)
correct=wordst1=""
score=0
while word :
   p=random.randrange(len(word))
   st1+=word[p]
   word=word[:p]+word[(p+1):]
print("""welcome to world of jumble games
unscramle the letters to make a wd
try to get the lowest score possible for each hin
tu gain points see if u can win with no points
for hint press h for exit press e""")
time.sleep(0.5)
print("the jumble word is ",st1)
guess=input("enter ur guess")
guess=guess.lower()
while True:
    if guess==correct:
        print("correct guess,your score is ",score)
        break
        
    elif guess=="h":
        n = range(len(correct))
        k=random.choice(n)
        print(correct[k],"is the", k+1," letter ")
        time.sleep(1)
        score=score+1
        guess=input("hint or exit or guess")
        time.sleep(1)
        guess=guess.lower()
    elif guess=="e":
        print("sorry u gave up ")
        break
    else :
        print("try again,wrong guess")
        guess=input("hint exit or guess")
    
