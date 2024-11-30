# Function to generate Fibonacci series up to 'n' terms
def fibonacci_series(n):
    # Initial two terms of the Fibonacci series
    fib_series = [0, 1]
    
    # Check if the number of terms is less than or equal to 0
    if n <= 0:
        return "Please enter a positive integer."
    # If the user wants only the first term
    elif n == 1:
        return [0]
    # If the user wants only the first two terms
    elif n == 2:
        return fib_series
    else:
        # Generate the series up to 'n' terms
        while len(fib_series) < n:
            next_term = fib_series[-1] + fib_series[-2]
            fib_series.append(next_term)
        return fib_series

# Input from the user
num_terms = int(input("Enter the number of terms: "))

# Generate and display the Fibonacci series
print("Fibonacci series:", fibonacci_series(num_terms))
