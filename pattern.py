"""result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or (row == 6 and column != 0 and column < 6)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str)
"""
x=""
i=0
while i<6:
    j=0
    while j<6:
        if (j==1 or (i==6 and j!=0 and j<6)):
            print(""+"*")
        else:
            print("")
print(x)

    
