def calculate(num1, num2, operation):
    """
    Performing a mathematical operation on two numbers.
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        # Handle division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."
        # Getting user input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Performing the calculation and print the result
    result = calculate(num1, num2, operation)
    if isinstance(result, str):
        print(result)
    else:
        print(f"{num1} {operation} {num2} = {result}")

except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
