def transpose(matrix):
  """
  Calculates the transpose of a matrix.

  Args:
    matrix: The matrix to be transposed.

  Returns:
    The transpose of the matrix.
  """

  n = len(matrix)
  m = len(matrix[0])

  transposed_matrix = []
  for i in range(m):
    transposed_row = []
    for j in range(n):
      transposed_row.append(matrix[j][i])
    transposed_matrix.append(transposed_row)

  return transposed_matrix


if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

  transposed_matrix = transpose(matrix)

  print(transposed_matrix)
  # This will print the following matrix:
  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
#This code first defines a function called transpose(). This function takes a matrix as an argument and returns the transpose of the matrix.

#The code then defines a main function that calls the transpose() function with the matrix matrix. This will print the transposed matrix to the console.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as transpose.py, you can run it by typing the following command into the command line:

