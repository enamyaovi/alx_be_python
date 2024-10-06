#This is going to be my first python script file for the ALx Program. Let's GO!

# Defining the predetermined variables
number1 = 10
number2 = 5

# Here are some basic operations performed on the two variables
def operations(number1:int, number2:int):
    """"This function returns the sum, difference and product of 
    two predefined integers (10 and 5)"""

    sum_of_numbers = number1 + number2
    diff_of_numbers = number1 - number2
    prod_of_numbers = number2 * number1
    return sum_of_numbers, diff_of_numbers, prod_of_numbers

#onto the print commands
def main():

    sum_of_numbers, diff_of_numbers, prod_of_numbers = operations(number1, number2)

    print('assuming the number1 = ' +str(number1)+ ' and the number2= '+str(number2))
    print('Addition of ' +str(number1) +' and ' +str(number2) +' is ' + str(sum_of_numbers))
    print('Subtraction between ' +str(number1) +' and ' +str(number2) +' is ' + str(diff_of_numbers))
    print('Multiplication of ' +str(number1) +' and ' +str(number2) +' is ' + str(prod_of_numbers))

if __name__ == '__main__':
    main()
