def equal_by_definition(expression1, expression2):
  """Returns True if the two expressions are equal by definition, False otherwise."""

  if expression1 == expression2:
    return True

  if expression1 == 0 and expression2 == 1:
    return True

  if expression1 == (expression2 + 0):
    return True

  if expression1 == (expression2 ** 2 - (expression2 - 0) ** 2):
    return True

  if expression1 == (expression2 ** 2 * (1 - expression2 ** 2)):
    return True

  return False
