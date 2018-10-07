# program to run the collatz sequence
def collatz(number):
    if number % 2 == 0:
        return(number // 2)
    elif number % 2 == 1:
        return(3 * number + 1)

# print(collatz(21))        

print('Please enter a number')
try:  
    userInput = int(input())
except ValueError:
    print('Error: Please enter a NUMBER.')
    userInput = int(input())

# print(collatz(userInput))

while userInput != 1:
    userInput = (collatz(userInput))
    print(userInput)
