#calculator.py# Basic Calculator Program
# This program performs basic arithmetic operations: addition, subtraction, multiplication, and division.

#global variables
welcome_message = "\nWelcome to the Basic Calculator!"
program_description = "This program performs basic arithmetic operations: addition, subtraction, multiplication, and division."
exit_message = "Thank you for using the Basic Calculator! Goodbye! 👋\n"
answer = None  # Initialize answer variable
operations = [
    ('Addition', '+'),
    ('Subtraction', '-'),
    ('Multiplication', '*'),
    ('Division', '/')
]

# function to ask the user for their name
# It will prompt the user to enter their name and return it
# If the user doesn't enter a name, it will default to "Dear"
def ask_name():
    username = input("Tell me your name, and let's get to it 💪 : ").strip()
    if username == "" or username.isspace() or  type(username) != str:
        print("You didn't enter a name, but that's okay! I'll just call you 'Dear' 😇 \n")
        username = "Dear"  # Default name if user doesn't provide one
    else:
        print(f"{username}, nice name!😉 Now let's do some calculations.\n")
    return username

# function to check if the operator is valid
# It will prompt the user to enter an operator and validate it
def  check_operator():
    valid_operators = [operation for _, operation in operations] # List of valid operators
    unknown_operator = input("Enter an operator (+, -, *, /): ").strip()
    i = 0    
    while unknown_operator not in valid_operators and i < 3: #Retry loop; up to 3 times
        print("\now! 🫨   Operator should be one of these:")
        for name, operation in operations: # List valid operations
            print(f"{name}: {operation}")
        unknown_operator = input(f"\nAttempt {3 - i} / 3...Try again: ").strip()
        i += 1
    if unknown_operator not in valid_operators:
        print("Too many invalid attempts.")
        return None          
    return unknown_operator

# function to check if the input is a valid float
# It will prompt the user to enter a number and validate it
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
    operand1 = check_floats(prompt = "Enter the first number: ")
    if operand1 is None:
        return None, None  # Return None if input is invalid
    operand2 = check_floats(prompt = "Enter the second number: ")
    return operand1, operand2

# function to perform the calculation based on the operator
# It takes two operands and an operator, performs the calculation, and returns the result
# boolean value indicates success or failure, and the result or error message
def calculator(operand1, operand2):
    operator = check_operator()
    if operator is None:
        return [False, "Invalid operator"]
    if operator == '+':
        return [True, operand1 + operand2]
    elif operator == '-':
        return [True, operand1 - operand2]
    elif operator == '*':
        return [True, operand1 * operand2]
    elif operator == '/':
        if operand2 == 0:
            return [False, "Division by zero is not allowed."]
        return  [True, operand1 / operand2]
 
#fuction to call calculator and display the result
# It takes the username, gets the operands, performs the calculation, and displays the result   
#calls calculator function and handles the result
def run_program(username):
    operand1, operand2 = take_values()  # Get the numbers from the user
    all_good = isinstance(operand1, float) and isinstance(operand2, float)
    if not all_good:
        print(f"\nError: invalid input for numbers.")
        return    
    answer = calculator(operand1, operand2)  # Perform the calculation
    if answer[0]:
        print(f"{username}, The result of your calculation is: {answer[1]} ✌️")
    else:
        print(f"Error: {answer[1]}")  # If the calculation was successful

# Main function to run the calculator program
# It greets the user, describes the program, and handles the main loop for calculations
# It prompts the user to start/continue the calculator, or exit the program
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

# End of the Basic Calculator Program
