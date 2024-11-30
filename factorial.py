# Function to calculate factorial using iteration
def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Input from the user
num = int(input("Enter a number: "))

# Display the result
print(f"Factorial of {num} (Iterative): {factorial_iterative(num)}")
