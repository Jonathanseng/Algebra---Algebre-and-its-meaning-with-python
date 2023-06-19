def for_all(statement, set):
  """Returns True if statement is true for all elements in set."""
  for element in set:
    if not statement(element):
      return False
  return True

def main():
  """Prints whether the statement x² ≥ 0 is true for all real numbers."""
  statement = lambda x: x² >= 0
  set = {-10, -5, 0, 5, 10}

  print("The statement x² ≥ 0 is true for all real numbers:", for_all(statement, set))

if __name__ == "__main__":
  main()

  # This code defines a function called for_all() that takes a statement and a set as input and returns True if the statement is true for all elements in the set. The main function then calls the for_all() function with the statement x² ≥ 0 and the set of real numbers {-10, -5, 0, 5, 10}.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as for_all.py, you can run it by typing the following command at the command line:
