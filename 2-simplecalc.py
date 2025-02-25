print("Welcome to the Simple Calculator!")

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the operations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2  # num2 should not be 0 for now 

#print results
print(f"\nResults:")
print(f"Addition: {num1} + {num2} = {sum_result}")
print(f"Subtraction: {num1} - {num2} = {difference}")
print(f"Multiplication: {num1} * {num2} = {product}")
print(f"Division: {num1} / {num2} = {quotient}")
