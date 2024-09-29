# This project is about experimenting with the datetime module in python

import datetime




def display_current_datetime():
    """Understanding the Python DateTime Module"""

    current_date = datetime.datetime.now()
    parsed_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
    print(f'Current date and time: {parsed_date}')

    # prompting for user input needed for calculating future date
    number_of_days = int(input('Enter the number of days to add to the current date: '))
    time_delta = datetime.timedelta(days = number_of_days)

    def calculate_future_date():
        """Calculates the future date by user input"""

        future_date = (current_date + time_delta).strftime('%Y-%m-%d')
        print(f'Future date: {future_date}')
    calculate_future_date()

display_current_datetime()



 