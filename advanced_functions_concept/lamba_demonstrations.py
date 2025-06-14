# Lanbda are almost like the parentheses functions in JavaScript
# They are used to create small anonymous functions
# Lambda functions are often used for short, throwaway functions that are not reused elsewhere.
# They can be used in places where a function is required, such as in higher-order functions like map, filter, and reduce.
# They are defined using the lambda keyword, followed by a list of parameters, a colon, and an expression.
# They can take any number of parameters but can only have one expression.
# They are often used for simple operations that can be expressed in a single line.

def main():
  # Demonstrating lambda functions
  add = lambda x, y: x + y
  result = add(5, 3)
  print("Result of add(5, 3):", result)

  # using lambde with HO function
  scores = [100, 99, 25, 44, 85, 77, 64]
  filtered_scores = list(filter(lambda score: score > 50, scores))
  print("Filtered scores (greater than 50):", filtered_scores)
  # using lambda with map function
  doubled_scores = list(map(lambda score: score * 2, scores))
  print("Doubled scores:", doubled_scores)


if __name__ == "__main__":
  main()