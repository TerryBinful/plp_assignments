# Name: Terry
# Module: Python
# Assignment: Week 3
# Title: Control Flows and Functions

#  Instructions: Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
#                Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.


#global variables
welcome_message = "\nWelcome to the Discount Calculator!"
program_description = "This program calculates the final price after applying a discount."
exit_message = "Thank you for using theDiscount Calculator!! Goodbye! 👋\n"
answer = None  # Initialize answer variable

# function to ask the user for their name
# It will prompt the user to enter their name and return it
# If the user doesn't enter a name, it will default to "Dear"
def ask_name():
    username = input("Tell me your name, and let's get to it 💪 : ").strip()
    if username == "" or username.isspace() or  type(username) != str:
        print("You didn't enter a name, but that's okay! I'll just call you 'Dear' 😇 \n")
        username = "Dear"  # Default name if user doesn't provide one
    else:
        print(f"{username}, nice name!😉 Now let's do some pricing.\n")
    return username

def check_floats(prompt):
    i = 0
    while i < 3:
        try:
            return float(input(prompt))
        except ValueError:
            print(f"ow! 🫨   I only accept numbers at this stage...Attempt {i + 1} / 3")
            i += 1
    print("Too many invalid attempts 😓")
    return None

# function to take two float values from the user
# calls check_floats to ensure valid input
# Returns a tuple of two floats or None if input is invalid
def take_values():
    price = check_floats(prompt = "Enter the original price: ")
    if price is None:
        return None, None  # Return None if input is invalid
    discount_percent = check_floats(prompt = "Enter the discount, dont add the percent: ")
    return price, discount_percent

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
def run_program(username):
    price, discount_percent = take_values()  # Get the numbers from the user
    all_good = isinstance(price, float) and isinstance(discount_percent, float)
    if not all_good:
        print(f"\nError: invalid input for numbers.")
        return    
    answer = calculate_discount(price, discount_percent)  # Perform the calculation
    if answer == price:
        print(f"{username}, No discount applied, Price is: {answer}")
    else:
        print(f"{username}, {discount_percent}% discount applied, Price is now: {answer} ✌️")  # If the calculation was successful


def main():
    print(welcome_message) #Greet user
    print(program_description)  # Describe the program's functionality

    start = input("\nDo you want to start the calculator? (yes/no): ").strip().lower()
    if start in ['yes', 'y']:
        username = ask_name()  # Ask for user's name, add a personal touch

    while start == 'yes' or start == 'y':
        run_program(username)  # Run the calculator program
        start = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
    else:
        print("Okay, maybe next time! 😊")  # Exit message

main()  # Start the program
print(exit_message)
   