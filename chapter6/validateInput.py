while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new pasword (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Password can only have letters and numbers.')    

print('\nYou are now ' + str(age) + ' years old, but you are still using ' + password + ' as your password!! \n LOL')

