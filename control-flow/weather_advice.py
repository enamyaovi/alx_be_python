# This is a program written in python that gives weather advice to users

user_input = input("What's the weather like today? (sunny/rainy/cold): ").lower()
if user_input == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif user_input == "rainy":
    print("Don't forget your umbrella and raincoat.")
elif user_input == "cold":
    print("Make sure to wear a warm coat and scarf.")
else:
    print("Sorry, I don't have recommendations for this weather")

