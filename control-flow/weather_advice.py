# This is a program written in python that gives weather advice to users

user_input = input('what\'s the weather like today? (sunny/rainy/cold): ').strip().lower()

if user_input == 'sunny':
    print(f'Wear a t-shirt and sunglasses.')
elif user_input == 'rainy':
    print(f'Don\'t forget your umbrella and raincoat.')
elif user_input == 'cold':
    print(f'Make sure to wear a warm coat and scarf.')
else:
    print(f'Sorry, I don\'t have recommendations for this weather')

