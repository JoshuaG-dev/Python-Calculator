number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

if operation == "+": 
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")
elif operation == "-":
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")
elif operation == "*":
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")
elif operation == "/":
    if number2 != 0:
        result = number1 / number2
        print(f"{number1} / {number2} = {result}")
    else:
        print("Error: cannot divide by zero.")
else:
    print("Invalid Operation")