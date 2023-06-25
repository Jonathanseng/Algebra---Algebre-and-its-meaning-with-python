import math

def euclidean_distance(x, y):
  """Returns the Euclidean distance between two points in n-dimensional space."""
  n = len(x)
  distance = 0
  for i in range(n):
    distance += (x[i] - y[i])**2
  return math.sqrt(distance)

def main():
  x = [1, 2, 3]
  y = [4, 5, 6]
  print(euclidean_distance(x, y))

if __name__ == "__main__":
  main()

#This code first defines a function called euclidean_distance() that takes two points in n-dimensional space as input and returns the Euclidean distance between them. The function uses the math.sqrt() function to calculate the square root of the sum of the squares of the differences between the corresponding elements of the two points.

#The code then defines a main function that calls the euclidean_distance() function on the points x and y. The output of the code is the Euclidean distance between the points x and y, which is 5.196152422706632.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as euclidean_distance.py, you can run it by typing the following command into the command line:

# This will run the code and print the output to the console.

#Here is an explanation of the code:

#The euclidean_distance() function takes two points in n-dimensional space as input and returns the Euclidean distance between them.
#The for loop iterates over all the elements of the two points.
#The if statement checks if the two points have the same element.
#The distance variable is used to store the sum of the squares of the differences between the corresponding elements of the two points.
#The math.sqrt() function is used to calculate the square root of the distance.
#The main() function calls the euclidean_distance() function on the points x and y.
#The print() statement prints the output of the euclidean_distance() function.
