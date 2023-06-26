import math

def find_center_of_circle(x1, y1, x2, y2):
  """Finds the center of a circle given the endpoints of a diameter.

  Args:
    x1: The x-coordinate of the first endpoint of the diameter.
    y1: The y-coordinate of the first endpoint of the diameter.
    x2: The x-coordinate of the second endpoint of the diameter.
    y2: The y-coordinate of the second endpoint of the diameter.

  Returns:
    The center of the circle as a tuple of (x, y) coordinates.
  """

  center_x = (x1 + x2) / 2
  center_y = (y1 + y2) / 2
  return (center_x, center_y)

if __name__ == "__main__":
  x1 = 10
  y1 = 20
  x2 = 30
  y2 = 40
  center = find_center_of_circle(x1, y1, x2, y2)
  print(center)

# This code first defines a function called find_center_of_circle(). This function takes four arguments: the x-coordinates of the first and second endpoints of the diameter, and the y-coordinates of the first and second endpoints of the diameter. The function then uses the midpoint formula to calculate the center of the circle, and returns the center as a tuple of (x, y) coordinates.

#The main function of the code then defines the x- and y-coordinates of the first and second endpoints of the diameter, and calls the find_center_of_circle() function. The function then prints the center of the circle.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as center_of_circle.py, you can run it by typing the following command into the command line:
