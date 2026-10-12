# Good Coffee Sim

# Current Day Number
day = 1
# Sales list of dictionaries
#Sales = [
#    {
#        "day": 1,
#        "coffee_inv": 100,
#        "advertising": "10",
#        "temp": 68,
#        "cups_sold": 16
#    },
#    {
#        "day": 2,
#        "coffee_inv": 84,
#        "advertising": "15",
#        "temp": 72,
#        "cups_sold": 20
#    }, 
#    {
#        "day": 3,
#        "coffee_inv": 64,
#        "advertising": "5",
#        "temp": 78,
#        "cups_sold": 10
#]
# Create a empty sales list
sales = []


#Print Welcome Message

print("Welcome to Good Coffee Sim!")
print("------------------------------------------------\n")
print("Lets collect some info before we start the game!\n")

# Get name and shop name

name = input("What is your name? ")
shop_name = input("What do you want to name your Coffee Shop!\n")

print("\nThanks, " + name + ". Let's set some intial prices!\n")

# Get Intial Pricing for a cup of coffee
cup_price = input("What do you want the price for a cup of coffee to be?")

# Display what we got
print("\nGreat. Here's what we got so far.\n")
print("Your name is " + name + " and you're opening " + shop_name + "!")


print("Your first cup of coffee will sell for $ " + str(cup_price) + ".\n")