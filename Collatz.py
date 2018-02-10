# Peter Thornton, 10 Feb 18
# The Collatz Conjecture
# Reference: https://en.wikipedia.org/wiki/Collatz_conjecture

i = int(input("Please enter an integer: "))  
x = i

while i > 1:
    if i % 2 == 0:
        i = i / 2 
        print(i)
    else:
        i = (3 * i) + 1
        print(i) 


print("Number at start: ",x,"Number at end: ",i) 
