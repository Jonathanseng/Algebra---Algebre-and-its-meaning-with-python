def cube_root(number):
  """
  Calculates the cube root of a number.

  Args:
    number: The number to find the cube root of.

  Returns:
    The cube root of the number.
  """

  return number ** (1 / 3)


if __name__ == "__main__":
  print(cube_root(27))
  # This will print 3

  print(cube_root(64))
  # This will print 4
#This code first defines a function called cube_root(). This function takes one argument: the number to find the cube root of. The function then uses the ** operator to calculate the cube root of the number.

#The code then defines a main function that calls the cube_root() function with the arguments 27 and 64. This will print the values 3 and 4 to the console.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as cube_root.py, you can run it by typing the following command into the command line:
