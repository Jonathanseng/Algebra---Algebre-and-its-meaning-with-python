def there_exist(statement, set):
  """Returns True if there exists an element in set such that statement is true."""
  for element in set:
    if statement(element):
      return True
  return False

def main():
  """Prints whether there exists a real number x such that x² ≥ 0."""
  statement = lambda x: x² >= 0
  set = {-10, -5, 0, 5, 10}

  print("There exists a real number x such that x² ≥ 0:", there_exist(statement, set))

if __name__ == "__main__":
  main()
# This code defines a function called there_exist() that takes a statement and a set as input and returns True if there exists an element in the set such that the statement is true. The main function then calls the there_exist() function with the statement x² ≥ 0 and the set of real numbers {-10, -5, 0, 5, 10}.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as there_exist.py, you can run it by typing the following command at the command line:
