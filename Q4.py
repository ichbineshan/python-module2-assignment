# Write a program that asks the user for two numbers. Then ask them if they would like to 
# add, subtract, divide, or multiply these numbers.
# Perform the chosen operation on the values, showing the operation being performed.​
# Write four functions, one for each mathematical operation.​
# Example: add(), subtract(), Multiply(), and Divide()​

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

try:
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    
    print("Press A for Add")
    print("Press S for Subtract")
    print("Press M for Multiply")
    print("Press D for Divide")

    response = input()

    if response == 'A':
        print(a, "+", b, "=", add(a, b))
    elif response == 'S':
        print(a, "-", b, "=", subtract(a, b))
    elif response == 'M':
        print(a, "*", b, "=", multiply(a, b))
    elif response == 'D':
        print(a, "/", b, "=", divide(a, b))
    else:
        print("Please select from A/S/M/D ")     #to check if entered operation is invalid
        
        
except Exception as e:
    print("Please enter valid numbers!")         #to check if the input numbers are invalid



