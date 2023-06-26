def area_of_triangle(base, height):
  """
  Calculates the area of a triangle given the base and height.

  Args:
    base: The base of the triangle.
    height: The height of the triangle.

  Returns:
    The area of the triangle.
  """

  return (1 / 2) * base * height

if __name__ == "__main__":
  base = 10
  height = 5
  area = area_of_triangle(base, height)
  print("The area of the triangle is", area)

# This code first defines a function called area_of_triangle() that takes the base and height of a triangle as input and returns the area of the triangle. The function uses the formula Area = (1/2) * base * height to calculate the area. The code then defines a variable called base and assigns it the value 10. The code then defines a variable called height and assigns it the value 5. The code then calls the area_of_triangle() function, passing the values of base and height as input. The function returns the area of the triangle, which is then printed to the console.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as area_of_triangle.py, you can run it by typing the following command into the command line:
