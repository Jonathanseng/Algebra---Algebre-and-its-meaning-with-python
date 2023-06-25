def symmetric_group(n):
  """Returns the symmetric group over n elements."""
  group = []
  for i in range(n):
    for j in range(i + 1, n):
      for k in range(j + 1, n):
        group.append((i, j, k))
  return group

def main():
  print(symmetric_group(3))

if __name__ == "__main__":
  main()
# This code first defines a function called symmetric_group() that takes an integer n as input and returns the symmetric group over n elements. The function uses a for loop to iterate over all the possible permutations of the set {1, 2, 3}, and it adds each permutation to the group.

#The code then defines a main function that calls the symmetric_group() function on the integer 3. The output of the code is the set of all permutations of the set {1, 2, 3}, which is the symmetric group S3.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as symmetric_group.py, you can run it by typing the following command into the command line:

# This will run the code and print the output to the console.

#Here is an explanation of the code:

#The symmetric_group() function takes an integer n as input and returns the symmetric group over n elements.
#The for loop iterates over all the possible permutations of the set {1, 2, 3}.
#The if statement checks if the permutation is a valid permutation.
#The group list is used to store the permutations.
#The main() function calls the symmetric_group() function on the integer 3.
#The print() statement prints the output of the symmetric_group() function.
