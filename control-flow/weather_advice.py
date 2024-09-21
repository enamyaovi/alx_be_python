# This program suggests what to wear depending on the weather returned from the
# User's response in the prompt.

weather = input("What's the weather like today? (sunny/rainy/cold): ").lower().strip() # prompt for user to enter condition

#Conditionals to return clothing recommendation based on weather
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather")

