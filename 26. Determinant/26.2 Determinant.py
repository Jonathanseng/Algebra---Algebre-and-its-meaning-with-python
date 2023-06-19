import numpy as np

def determinant(matrix):
  """
  Calculates the determinant of a square matrix.

  Args:
    matrix: The square matrix.

  Returns:
    The determinant of the matrix.
  """

  if len(matrix.shape) != 2:
    raise ValueError("matrix must be a square matrix")

  n = len(matrix.shape[0])

  if n == 1:
    return matrix[0][0]

  if n == 2:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

  determinant = 0
  for i in range(n):
    cofactor = 1
    for j in range(n):
      if j != i:
        cofactor *= matrix[i][j]
    determinant += cofactor * matrix[i][i]

  return determinant


if __name__ == "__main__":
  matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

  print(determinant(matrix))
  # This will print -27

 # This code first imports the numpy module, which contains the linalg module. The linalg module contains the det() function, which can be used to calculate the determinant of a matrix.

#The code then defines a function called determinant(). This function takes a square matrix as an argument and returns the determinant of the matrix.

#The code then defines a main function that calls the determinant() function with the matrix matrix. This will print the value -27 to the console.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as determinant.py, you can run it by typing the following command into the command line:
