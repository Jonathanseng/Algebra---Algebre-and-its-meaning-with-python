def point(x, y):
  """Returns a point object with coordinates (x, y)."""
  return {"x": x, "y": y}

def distance(p1, p2):
  """Returns the distance between two points."""
  x1, y1 = p1["x"], p1["y"]
  x2, y2 = p2["x"], p2["y"]
  return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def main():
  p1 = point(1, 2)
  p2 = point(3, 4)
  print(distance(p1, p2))

if __name__ == "__main__":
  main()

# This code defines a function called point() that takes two numbers as input and returns a point object with those coordinates. The distance() function then takes two point objects as input and returns the distance between them. The main() function creates two point objects and then prints the distance between them.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as point.py, you can run it by typing the following command into the command line:
# This will print the distance between the two points, which is 2.8284271247461903.
