def floor_bracket(x):
  """Returns the floor bracket of x."""

  if x < 0:
    return int(x) - 1
  else:
    return int(x)


def main():
  print(floor_bracket(2.3))
  print(floor_bracket(-2.3))


if __name__ == "__main__":
  main()

  # This code defines a function called floor_bracket() that takes a number as input and returns the floor bracket of the number. The function uses the int() function to convert the number to an integer, and then it checks if the number is negative. If the number is negative, the function subtracts 1 from the integer. Otherwise, the function simply returns the integer.

#The code also includes a main function that tests the floor_bracket() function with a few different numbers. The output of the main function shows that the function correctly returns the floor bracket of the numbers.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as floor_bracket.py, you can run it by typing the following command into the command line:

#This will run the main function and print the output to the console.

#The code can be modified to include other methods for calculating the floor bracket of a number. For example, you could use the math.floor() function to calculate the floor bracket of a number.

#The code can also be modified to take a different type of input, such as a string or a list of numbers. For example, you could modify the code to take a string as input and return the floor bracket of the first number in the string.
