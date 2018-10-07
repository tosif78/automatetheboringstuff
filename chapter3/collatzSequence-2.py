# program to run the collatz sequence
def collatz(number):
    if number % 2 == 0:
        return(number // 2)
    elif number % 2 == 1:
        return(3 * number + 1)
    
while True:
    try:  
        print('Please enter a number')
        userInput = int(input())
        break
    except ValueError:
        print('Error: Please enter a NUMBER.')

while userInput != 1:
    userInput = (collatz(userInput))
    print(userInput)
