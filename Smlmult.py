# Peter Thornton, 17 Feb 2018
# Smallest multiple of all numbers between 1-20
# https://projecteuler.net/problem=5

# Problem Statement

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Setting Range

Max = 20
Min = 1

End = Max + 1

print("This program will define the smallest multiple of every number between a range. This is pre-set to 1 to 20.")

# Q: User set a range?

if input("Would you like to change the range? (Y/N): ") == "Y":
    Max = int(input("Max: "))
    Min = int(input("Min: "))
    End = Max + 1


# Is the number divisible by all numbers in range?
def ChkDivisible(x):
    for i in range(Min,End):
        if x % i != 0:
            return False
    return True

# Start at 1, run ChkDivisible until True
x = Max 
while True:
    if ChkDivisible(x):
        break
    x = x + Max

print(x)