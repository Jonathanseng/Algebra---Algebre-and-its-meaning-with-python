def summation(start, end):
  """
  Calculates the sum of the numbers from start to end.

  Args:
    start: The starting value of the sum.
    end: The ending value of the sum.

  Returns:
    The sum of the numbers from start to end.
  """

  sum = 0
  for i in range(start, end + 1):
    sum += i

  return sum


if __name__ == "__main__":
  print("The sum of the numbers from 1 to 10 is", summation(1, 10))

  #This code first defines a function called summation() that takes the starting and ending values of the sum as input and returns the sum of the numbers from start to end. The function then uses a for loop to iterate over the numbers from start to end, and it adds each number to the sum variable. The sum variable is then returned by the function.

#The main function of the code then assigns the values 1 and 10 to the starting and ending values of the sum, respectively. It then calls the summation() function to calculate the sum of the numbers from 1 to 10. The result of the calculation is then printed to the console.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as summation.py, you can run it by typing the following command into the command line:
