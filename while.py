"""#addition of 1st 10 nos
x = 0
s = 0
while (x < 11):
     s = s + x
     x = x + 1
else :
     print('The sum of first 9 integers : ',s)
     
#sorting
a = [7,8,9,0,1,2,3,4,5,6,]

i = 0
while(i < len(a)):
    j = 0
    while(j < len(a) - i - 1):
        if(a[j] > a[j + 1]):
             temp = a[j]
             a[j] = a[j + 1]
             a[j + 1] = temp
        j = j + 1
    i = i + 1

print("The Sorted List in Ascending Order : ", a)

#fibonnaci series
The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
x,y=0,1

while y<50:
    print(y)
    x,y = y,x+y
    
lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
        print(lines)
    else:
        break
        
i=1                                                                      
while(i<=5):                                                                                                                                          
    print("   ")                                                         
    j=1                                                                    
    while(j<=i):                                                                                                                                 
        print(" * ")                                                      
        j+=1                                                                                                                                       
    print("\n")                                                          
    i+=1 """                                                                       
i=1 
while i<10: 
    print ("3","x",i,"=",i*3) 
    i+=1
    """
i=0
ch = 'A'
while i<10:
# Using chr()+ord() 
# prints P 
   x = chr(ord(ch) + 1) 
  
   print ("The incremented character value is : ",end="") 
   print (x)
   """
