def inner_product(u, v):
  """
  Calculates the inner product of two vectors.

  Args:
    u: The first vector.
    v: The second vector.

  Returns:
    The inner product of the two vectors.
  """

  sum = 0
  for i in range(len(u)):
    sum += u[i] * v[i]

  return sum


if __name__ == "__main__":
  u = [1, 2, 3]
  v = [4, 5, 6]

  print(inner_product(u, v))
  # This will print 32

  #This code first defines a function called inner_product(). This function takes two vectors as arguments and returns the inner product of the two vectors.

#The code then defines a main function that calls the inner_product() function with the vectors u and v. This will print the value 32 to the console.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as inner_product.py, you can run it by typing the following command into the command line:
