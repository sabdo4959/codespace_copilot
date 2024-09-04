from main import add, subtract, multiply, divide

# Test cases for the add function
assert add(5, 3) == 8
assert add(-2, 7) == 5
assert add(0, 0) == 0

# Test cases for the subtract function
assert subtract(10, 7) == 3
assert subtract(5, 5) == 0
assert subtract(100, 50) == 50

# Test cases for the multiply function
assert multiply(4, 6) == 24
assert multiply(0, 10) == 0
assert multiply(-3, 5) == -15

# Test cases for the divide function
assert divide(8, 2) == 4
assert divide(10, 3) == 3.3333333333333335
assert divide(100, 0) == "Error: Division by zero"

print("All test cases passed!")