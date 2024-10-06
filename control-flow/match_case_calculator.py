# This script is in three levels
# First receives input from users, then asks for arithmetic operation and returns the results
# match case block is implemented for the operation to avoid writing spaghetti if statements



# variables for prompting user for numbers and operator
while True:
    try:
        num1: int = int(input('Enter the first number: '))
        num2: int = int(input('Enter the second number: '))
        operation: str = input('Choose the operation (+, -, *, /): ')
    except ValueError:
        print(f'You have entered the wrong input, please enter a numeric value like: 1, 2, 3 ...')
    else:
        print(f'Your numbers are {num1} and {num2}. Selected Operation is {operation}')
        break
    finally:
        print('Finally Block: Executes no matter what.')
        

    



# match case block for different operation scenarios
match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num2 * num1
    case '/':
        if num2 == 0:  #this if statement is to prevent a zerodivision error in case denominator is zero
            print('Cannot divide by zero.')
            quit()
        else:
            result = num1/num2
        
print(f'The result is {int(result)}')