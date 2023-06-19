def discriminant(a, b, c):
  """
  Calculates the discriminant of a quadratic equation.

  Args:
    a: The coefficient of x² in the quadratic equation.
    b: The coefficient of x in the quadratic equation.
    c: The constant term in the quadratic equation.

  Returns:
    The discriminant of the quadratic equation.
  """

  return b**2 - 4 * a * c


if __name__ == "__main__":
  a = 1
  b = -4
  c = 4

  discriminant_value = discriminant(a, b, c)

  print("The discriminant of the quadratic equation is", discriminant_value)

  #This code first defines a function called discriminant() that takes the coefficients of a quadratic equation as input and returns the value of the discriminant. The function then uses the formula b**2 - 4 * a * c to calculate the discriminant.

#The main function of the code then assigns the values 1, -4, and 4 to the coefficients a, b, and c, respectively. It then calls the discriminant() function to calculate the discriminant of the quadratic equation. The result of the calculation is then printed to the console.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as discriminant.py, you can run it by typing the following command into the command line:

