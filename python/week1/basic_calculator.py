welcome_message = "\nWelcome to the Basic Calculator!"
program_description = "This program performs basic arithmetic operations: addition, subtraction, multiplication, and division."
exit_message = "Thank you for using the Basic Calculator! Goodbye! 👋\n"
username = "Dear"  # Default name if user doesn't provide one
operations = [
    ('Addition', '+'),
    ('Subtraction', '-'),
    ('Multiplication', '*'),
    ('Division', '/')
]

def ask_name():
    global username
    username = input("Tell me your name, and let's get to it 💪 : ").strip()
    if username == "" or username.isspace() or  type(username) != str:
        print("You didn't enter a name, but that's okay! I'll just call you 'Dear' 😇 \n")
        username = "Dear"
    else:
        print(f"{username}, nice name!😉 Now let's do some calculations.\n")
    return username



def  check_operator():
    unknown_operator = input("Enter an operator (+, -, *, /): ").strip()
    i = 0    
    while unknown_operator not in ['+', '-', '*', '/'] and i < 3:
        print("ow! 🫨   Operator should be one of these:")
        for operation in operations:
            print(operation)
        unknown_operator = input().strip()
        i += 1
    if unknown_operator not in ['+', '-', '*', '/']:
        print("Too many invalid attempts.")
        return None          
    return unknown_operator

def  check_floats():
    floating_number = float(input())
    i = 0    
    while  type(floating_number) != float and i < 3:
        print("ow! 🫨   I only accept numbers at this stage:")
        print("Please enter a valid number:")
        floating_number = float(input())
        i += 1
    if type(floating_number) != float:
        print("Too many invalid attempts.")
        return None          
    return floating_number

def take_values():
    
    print("Enter the first number: ")
    operand1 = check_floats()
    if operand1 is None:
        return [False, "Invalid value for the first number."]
    print("Enter the second number: ")
    operand2 = check_floats()
    if operand1 is None:
        return [False, "Invalid value for the second number."]
    return operand1, operand2


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
        if operand2 != 0:
            return  [True, operand1 / operand2]
        else:
            return [False, "Division by zero is not allowed."]
    else:
        return [True, "Invalid operator."]
 

def run_program():
    operand1, operand2 = take_values()  # Get the numbers from the user
    if isinstance(operand1, float) and isinstance(operand2, float):
       answer = calculator(operand1, operand2)  # Perform the calculation
    else:  # If there was an error
        print(f"Error: invalid input for numbers.")
    

    if answer[0]:  # If the calculation was successful
        print(f"{username}, The result of your calculation is: {answer[1]} ✌️")
    else:  # If there was an error
        print(f"Error: {answer[1]}")
   

def main():
    print(welcome_message) #Greet user
    print(program_description)  # Describe the program's functionality

    start = input("\nDo you want to start the calculator? (yes/no): ").strip().lower()
    ask_name()  # Ask for user's name, add a personal touch

    while start == 'yes' or start == 'y':
        run_program()  # Run the calculator program
        start = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
    else:
        print("Okay, maybe next time! 😊")  # Exit message

main()  # Start the program
print(exit_message)
