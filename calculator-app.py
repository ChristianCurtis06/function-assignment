# Task 1: Create functions for each arithmetic operation
def addition(number_1, number_2):
    sum = number_1 + number_2
    print(f"{number_1} plus {number_2} is {round(sum, 3)}.")

def subtraction(number_1, number_2):
    difference = number_1 / number_2
    print(f"{number_1} minus {number_2} is {round(difference, 3)}.")

def multiplication(number_1, number_2):
    product = number_1 * number_2
    print(f"{number_1} times {number_2} is {round(product, 3)}.")

def division(number_1, number_2):
    quotient = number_1 / number_2
    print(f"{number_1} divided by {number_2} is {round(quotient, 3)}.")

# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use
print("Calculator App:")

while True:
    operation_input = input("\nWhich operation would you like to perform? ([A]ddition, [S]ubtraction, [M]ultiplication, or [D]ivision) ").upper()
    if operation_input == "A" or operation_input == "S" or operation_input == "M" or operation_input == "D":
        break
    else:
        print("Invalid input. Please try again.")

number_1_input = float(input("\nWhat is the first number you would like to use in the equation? "))
number_2_input = float(input("What is the second number you would like to use? "))

# Task 3: Ensure your code can handle division by zero and other potential errors    
if operation_input == "A":
    addition(number_1_input, number_2_input)
elif operation_input == "S":
    subtraction(number_1_input, number_2_input)
elif operation_input == "M":
    multiplication(number_1_input, number_2_input)
elif operation_input == "D":
    try:
        division(number_1_input, number_2_input)
    except ZeroDivisionError:
        print("You cannot divide by 0.")