# This script prints out a reminder or note based on task priority level and urgency 


# prompts for receiving input from user 
task = input('Enter your task: ').strip().capitalize()
priority = input('Priority (high/medium/low): ').lower().strip()
time_bound = input('Is it time-bound? (yes/no):').lower().strip()

#variables for creating custom statements
message = ''
custom_message = ''

#match and case block for priority level nested with if statements for task urgency
#just trying something over here
match priority:
    case 'high':
        if time_bound == 'yes':
            message += f'Reminder:'
            custom_message += f' that requires immediate attention today!'
        else:
            message += f'Note:'
            custom_message += f'. Consider completing it when you have free time.'
    case 'medium':
        if time_bound == 'yes':
            message += f'Reminder:'
            custom_message += f' that requires immediate attention today!'
        else:
            message += f'Note:'
            custom_message += f'. Consider completing it when you have free time.'
    case 'low':
        if time_bound == 'yes':
            message += f'Reminder:'
            custom_message += f' that requires immediate attention today!'
        else:
            message += f'Note:'
            custom_message += f'. Consider completing it when you have free time.'

print(f"{message} '{task}' is a {priority} priority task{custom_message}") # prints custom message calling on various variables 