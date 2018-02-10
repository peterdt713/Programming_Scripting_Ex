# Week 1
# Peter Thornton
# College W1 Exc

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 34
ans = fib(x)
print("Fibonacci number", x, "is", ans)

# Comment in discussion form: My name is Peter, the first and last letter of my name (P + R = 16 + 18) give the number  34. The 34th Fibonacci number is 5,702,887.

# Week 2
# Peter Thornton
# College W2 Exc

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Thornton"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

# Comment in discussion fourm:

# My surname is Thornton

# The first letter T is number 84

# The last letter n is number 110

# Fibonacci number 194 is 15635695580168194910579363790217849593217

# The ord() method returns an integer representing Unicode code point for the given Unicode character.
