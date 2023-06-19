def power(base, exponent):
  """
  Calculates the power of a number.

  Args:
    base: The base number.
    exponent: The exponent.

  Returns:
    The power of the number.
  """

  if exponent == 0:
    return 1
  elif exponent == 1:
    return base
  else:
    return base * power(base, exponent - 1)


if __name__ == "__main__":
  print(power(2, 5))
  # This will print 32

  print(power(3, 2))
  # This will print 9

  #This code first defines a function called power(). This function takes two arguments: the base number and the exponent. The function then uses a recursive approach to calculate the power of the number. If the exponent is 0, the function returns 1. If the exponent is 1, the function returns the base number. Otherwise, the function multiplies the base number by the result of calling the power() function recursively with the exponent decremented by 1.

#The code then defines a main function that calls the power() function with the arguments 2 and 5. This will print the value 32, which is 2 raised to the 5th power. The code then calls the power() function with the arguments 3 and 2. This will print the value 9, which is 3 raised to the 2nd power.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as power.py, you can run it by typing the following command into the command line:
