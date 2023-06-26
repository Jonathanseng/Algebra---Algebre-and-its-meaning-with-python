import math

def circumference(diameter):
  """
  Calculates the circumference of a circle given the diameter.

  Args:
    diameter: The diameter of the circle.

  Returns:
    The circumference of the circle.
  """

  pi = math.pi
  return 2 * pi * diameter

if __name__ == "__main__":
  diameter = 10
  circumference = circumference(diameter)
  print("The circumference of the circle is", circumference)

# This code first imports the math module, which provides access to mathematical functions, such as the pi constant. The code then defines a function called circumference() that takes the diameter of a circle as input and returns the circumference of the circle. The function uses the formula C = 2πd to calculate the circumference. The code then defines a variable called diameter and assigns it the value 10. The code then calls the circumference() function, passing the value of diameter as input. The function returns the circumference of the circle, which is then printed to the console.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as circumference.py, you can run it by typing the following command into the command line:
