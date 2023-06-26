def height_of_2d_figure(figure):
  """
  Calculates the height of a 2D figure.

  Args:
    figure: The 2D figure.

  Returns:
    The height of the figure.
  """

  top = figure[0]
  bottom = figure[-1]
  return bottom - top

if __name__ == "__main__":
  figure = [1, 2, 3, 4, 5]
  height = height_of_2d_figure(figure)
  print("The height of the figure is", height)

# This code first defines a function called height_of_2d_figure() that takes a 2D figure as input and returns the height of the figure. The function uses the following formula to calculate the height:

# where bottom is the bottom coordinate of the figure and top is the top coordinate of the figure. The code then defines a variable called figure and assigns it the list [1, 2, 3, 4, 5]. The code then calls the height_of_2d_figure() function, passing the value of figure as input. The function returns the height of the figure, which is then printed to the console.

# To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as height_of_2d_figure.py, you can run it by typing the following command into the command line:
