def factorial_iterative (n):
    if n < 0 :
        return "Factorial for neative numbers is undefined"
    result = 1
    for i in range (1, n+1):
        result *= i
    return result

num = int(input("Please enter number:"))
print ("The factorial is : ", factorial_iterative(num))