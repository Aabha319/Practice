import random 
chars = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM,.;;=-!@#$%^&*()_+'
length = int(input(' What is your password length ?'))
password = ' '
for x in range(length):
    password += random.choice(chars)
print(password)


"""
#if you want to print the password for 5 times
for p in range(5):
    password = ' '   
    for c in range(length):                  
        password += random.choice(chars)
    print(password)
"""

