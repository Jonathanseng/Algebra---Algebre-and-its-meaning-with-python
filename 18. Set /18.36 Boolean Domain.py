def is_boolean(value):
  """Returns True if value is a boolean, False otherwise."""
  if isinstance(value, bool):
    return True
  else:
    return False

def main():
  print(is_boolean(True))
  print(is_boolean(False))
  print(is_boolean(0))
  print(is_boolean("True"))

if __name__ == "__main__":
  main()

#This code first defines a function called is_boolean() that takes a value as input and returns True if the value is a boolean and False otherwise. The function uses the isinstance() built-in function to check the type of the input value.

#The code then defines a main function that calls the is_boolean() function on different values, including True, False, 0, and "True". The output of the code is as follows:
# As you can see, the is_boolean() function correctly identifies the boolean values True and False as booleans, and it correctly identifies the non-boolean values 0 and "True" as not being booleans.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as boolean_domain.py, you can run it by typing the following command into the command line:
