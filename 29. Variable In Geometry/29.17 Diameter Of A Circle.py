def diameter(radius):
  """
  Calculates the diameter of a circle given the radius.

  Args:
    radius: The radius of the circle.

  Returns:
    The diameter of the circle.
  """

  return 2 * radius

if __name__ == "__main__":
  radius = 5
  diameter = diameter(radius)
  print("The diameter of the circle is", diameter)

# This code first defines a function called diameter() that takes the radius of a circle as input and returns the diameter of the circle. The function uses the formula D = 2r to calculate the diameter. The code then defines a variable called radius and assigns it the value 5. The code then calls the diameter() function, passing the value of radius as input. The function returns the diameter of the circle, which is then printed to the console.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as diameter.py, you can run it by typing the following command into the command line:
