import sys
import time
q=["q1","q2","q3","q4"]
ans=["A","C","A","D"]
print("instructions")
print(q[0])
print("display options....a,b,c,d")
choice=input("enter your choice")
if choice==ans[0]:
    print("congrats!! you have won Rs.1000")
else:
    print("oops!! sorry!! wrong ans")
    sys.exit();
time.sleep(2)
print(q[1])
print("display options....a,b,c,d")
choice=input("enter your choice")
if choice==ans[1]:
    print("congrats!! you have won Rs.5000")
else:
    print("oops!! sorry!! wrong ans")
    sys.exit();
time.sleep(2)
print(q[2])
print("display options....a,b,c,d")
choice=input("enter your choice")
if choice==ans[2]:
    print("congrats!! you have won Rs.10000")
else:
    print("oops!! sorry!! wrong ans")
    sys.exit();
time.sleep(2)
print(q[3])
print("display options....a,b,c,d")
choice=input("enter your choice")
if choice==ans[3]:
    print("congrats!! you have won Rs.20000")
else:
    print("oops!! sorry!! wrong ans")
    sys.exit();
time.sleep(2)
