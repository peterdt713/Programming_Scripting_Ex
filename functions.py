# Peter Thornton, 02 Apr 18

# Please complete the following exercise this week. 
# Write a Python script containing a function called factorial() that takes a single input/argument which is a positive integer and returns its factorial. 
# The factorial of a number is that number multiplied by all of the positive numbers less than it. 
# For example, the factorial of 5 is 5x4x3x2x1 which equals 120. 
# You should, in your script, test the function by calling it with the values 5, 7, and 10.


# Creating the factorial function
def factorial(i):
    fact_i = 1
    for i in range(1, i + 1):
        fact_i = fact_i * i 
    return fact_i

# Test for 5
x = 1 * 2 * 3 * 4 * 5

print("Test for 5: ", x)
print("The factoral of 5 is: ", factorial(5))

# Test for 7
j = 1 * 2 * 3 * 4 * 5 * 6 * 7

print("Test for 7: ", j)
print("The factoral of 7 is: ", factorial(7))

# Test for 10
h = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10

print("Test for 10: ", h)
print("The factoral of 10 is: ", factorial(10))

if input("Would you like to input a new number? (Y/N): ") == "Y":
    z = int(input("Please enter an integer: "))
    print("The factoral of ", z, " is: ", factorial(z))