def union(set1, set2):
  """Returns the union of two sets."""
  union_set = set1 | set2
  return union_set

def intersection(set1, set2):
  """Returns the intersection of two sets."""
  intersection_set = set1 & set2
  return intersection_set

def difference(set1, set2):
  """Returns the difference of two sets."""
  difference_set = set1 - set2
  return difference_set

def symmetric_difference(set1, set2):
  """Returns the symmetric difference of two sets."""
  symmetric_difference_set = set1 ^ set2
  return symmetric_difference_set

def main():
  """Prints the results of set operations."""
  set1 = {1, 2, 3, 4, 5}
  set2 = {2, 3, 4, 6, 7}

  print("The union of set1 and set2 is:", union(set1, set2))
  print("The intersection of set1 and set2 is:", intersection(set1, set2))
  print("The difference of set1 and set2 is:", difference(set1, set2))
  print("The symmetric difference of set1 and set2 is:", symmetric_difference(set1, set2))

if __name__ == "__main__":
  main()

  #This code defines four functions for performing set operations: union, intersection, difference, and symmetric difference. The main function then creates two sets, set1 and set2, and prints the results of calling the four functions on these sets.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as set_algebra.py, you can run it by typing the following command at the command line:

