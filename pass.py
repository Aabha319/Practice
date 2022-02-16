print('Enter correct username and password combo to continue')
count=0
while count < 4:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='Hytu76E' and username=='bank_admin':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1
