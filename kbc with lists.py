import sys
import time
score=0
ans_a=["A","a"]
ans_b=["B","b"]
ans_c=["C","c"]
ans_d=["D","d"]
print("instruction")
print("q1")
print("""A.Delhi
B Mumbai
C.pune
D.Banglore""")
choice=input("enter your choice")
if choice in ans_a:
    score+=1
    print("correct answer!! congratulations, you won Rs.1000")
else:
    print("Wrong answer!! sorry")
    sys.exit();
