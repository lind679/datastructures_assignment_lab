def fibonacci_series (n):
    # Initial two terms of the series
    fib_series = [0, 1]

    if n < 0:
        return "Please enter positive integer"
    elif n == 1:
        return [0]
    elif n == 2:
        return fib_series
    else:
        while len(fib_series) < n:
            next_term = fib_series[-1] + fib_series[-2]
            fib_series.append(next_term)
        return fib_series
    
num_terms = int(input("Please enter the number of terms :"))
print("The fibonacci series is :", fibonacci_series(num_terms))