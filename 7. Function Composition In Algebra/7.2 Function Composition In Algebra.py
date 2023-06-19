def f(x):
  """Returns the square of x."""
  return x * x

def g(x):
  """Returns x + 3."""
  return x + 3

def h(x):
  """Returns the composition of f and g."""
  return g(f(x))

print(h(3))

# This code defines three functions: f, g, and h. The function f returns the square of its input, the function g returns its input plus 3, and the function h returns the composition of the functions f and g.

#The code then prints the output value of the function h for the input value 3. The output value is 9, which is the square of 3 plus 3.

#To run this code, you can save it as a file named function_composition.py and then run it from the command line using the following command:

# This will print the output value of the function, which is 9.

#Here is an explanation of the code:

#The first line defines the function f. The function takes an input value, x, and returns the square of x.
#The second line defines the function g. The function takes an input value, x, and returns x plus 3.
#The third line defines the function h. The function takes an input value, x, and returns the composition of the functions f and g. The composition of f and g is defined as g(f(x)), which means that the function g is applied to the result of applying the function f to x.
#The fourth line prints the output value of the function h for the input value 3.
