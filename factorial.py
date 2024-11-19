#factorial function using recursion
def factorial(n): #function definition
    if n == 0: #base case
        return 1
    else:
        return n * factorial(n-1) #recursive call
# Test the factorial function
print(factorial(5)) #120
print(factorial(10)) #3628800
print(factorial(0)) 
