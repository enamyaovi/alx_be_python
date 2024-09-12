#This file helps users calculate their monthly savings

#defining variables from user inputs
month_inc = int(input('Enter your monthly income: '))
month_exp = int(input('Enter your monthly expenses: '))

#new variables
month_save = month_inc - month_exp
rate = 0.05
projected_save = month_save * 12 + (month_save * 12 * 0.05) #calculates the projected savings at 5% interest rate

r_projected_save = int(projected_save)

print('Your monthly savings are $' +str(month_save)+ '.')
print('Projected savings after one year, with interest, is: $'+str(r_projected_save)+'.')

