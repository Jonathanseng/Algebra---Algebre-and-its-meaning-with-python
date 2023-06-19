import math


def square_root(number):
  """
  Calculates the square root of a number.

  Args:
    number: The number to find the square root of.

  Returns:
    The square root of the number.
  """

  return math.sqrt(number)


if __name__ == "__main__":
  print(square_root(9))
  # This will print 3

  print(square_root(16))
  # This will print 4

  #This code first imports the math module, which contains the sqrt() function. The sqrt() function calculates the square root of a number.

#The code then defines a function called square_root(). This function takes one argument: the number to find the square root of. The function then uses the sqrt() function from the math module to calculate the square root of the number.

##The code then defines a main function that calls the square_root() function with the arguments 9 and 16. This will print the values 3 and 4 to the console.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as square_root.py, you can run it by typing the following command into the command line:
