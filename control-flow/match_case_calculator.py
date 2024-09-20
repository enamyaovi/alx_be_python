# This is a simple calculator that tests my understanding of how to implement the match case

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

oper_and = input(f'Choose the operation, (+,-,*,/): ')

match oper_and:
    case '+':
        result = num1 + num2
        print(f'The result is {int(result)}')
    case '-':
        result = num1 - num2
        print(f'The result is {int(result)}')
    case '*':
        result = num2 * num1
        print(f'The result is {int(result)}')
    case '/':
        if num2 == 0:
            print('Cannot divide by zero.')
            exit()
        result = num1/num2
        print(f'The result is {int(result)}')
    