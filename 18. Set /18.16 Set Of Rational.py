import fractions


def set_rational_numbers():
  """Returns a set of rational numbers."""
  set_of_rational_numbers = {
      fractions.Fraction(x, y) for x in range(10) for y in range(10) if x != 0 and y != 0
  }
  return set_of_rational_numbers


if __name__ == "__main__":
  set_of_rational_numbers = set_rational_numbers()
  print(set_of_rational_numbers)

# This code first imports the fractions module from the Python standard library. This module provides a class called Fraction that can be used to represent rational numbers.

#The set_rational_numbers() function then creates a set of rational numbers. The function works by first creating a range of integers from 1 to 10. Then, it iterates through the range and creates a Fraction object for each pair of integers. Finally, it adds each Fraction object to the set.

#The if __name__ == "__main__": block is used to execute the code if the file is being run as a script. In this case, the code will first create a set of rational numbers. Then, it will print the set to the console.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as set_rational_numbers.py, you can run it by typing the following command into the command line:
