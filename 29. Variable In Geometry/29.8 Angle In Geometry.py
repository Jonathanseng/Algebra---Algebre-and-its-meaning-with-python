import math

def angle_between_rays(ray1, ray2):
  """Returns the angle between the two rays in degrees."""
  x1, y1 = ray1
  x2, y2 = ray2
  dx = x2 - x1
  dy = y2 - y1
  angle = math.atan2(dy, dx) * 180 / math.pi
  if angle < 0:
    angle += 360
  return angle

def main():
  ray1 = (0, 0)
  ray2 = (10, 10)
  angle = angle_between_rays(ray1, ray2)
  print("The angle between the two rays is", angle)

if __name__ == "__main__":
  main()

# This code defines a function called angle_between_rays(), which calculates the angle between two rays in degrees. The function takes two points as input, and it returns the angle between the rays that start at those points. The main function then calls the angle_between_rays() function to calculate the angle between the rays that start at the points (0, 0) and (10, 10). The results are then printed to the console.

#To run this code, you will need to have Python installed on your computer. You can then save the code as a .py file and run it from the command line. For example, if you save the code as angle.py, you can run it by typing the following command into the command line:
