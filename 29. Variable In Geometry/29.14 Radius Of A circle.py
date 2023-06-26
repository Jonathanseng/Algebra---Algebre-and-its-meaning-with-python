import math

def radius_of_circle(diameter):
  """
  Calculates the radius of a circle given the diameter.

  Args:
    diameter: The diameter of the circle.

  Returns:
    The radius of the circle.
  """

  radius = diameter / 2
  return radius

if __name__ == "__main__":
  diameter = 10
  radius = radius_of_circle(diameter)
  print("The radius of the circle is", radius)

# This code first imports the math module, which contains the mathematical constant pi. Then, it defines a function called radius_of_circle() that takes a diameter as input and returns the radius of the circle. The function first calculates the radius by dividing the diameter by 2. Then, it returns the radius.

#The main function of the code takes a diameter as input and calls the radius_of_circle() function to calculate the radius. Then, it prints the radius.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as radius.py, you can run it by typing the following command into the command line:

