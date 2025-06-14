"""
This module demonstrates the concept of closures in Python.
Closures are functions that capture the local state of their enclosing scope,
allowing them to access variables from that scope even after it has finished executing.

Javascript closures are similar, where inner functions can access variables from their outer function's scope.

closure are used in the really world, for example, in event handlers, callbacks, and asynchronous programming.
In Javacript , closures are often used to create private variables and functions, it like class

let' make a simple example of a closure in Python:
"""

def outer_function(x):
  """
  This is the outer function that takes a parameter x.
  It defines an inner function that captures the value of x.
  """
  def inner_function(y):
    """
    This is the inner function that takes a parameter y.
    It uses the captured value of x to perform a calculation.
    x are alwways available in the inner function
    """
    return f"the outer function captured {x} and the inner function received {y}, and their sum is {x + y}"
  return inner_function

def main():
  first_number = 5
  second_number = 10
  # Create a closure by calling the outer function with first_number
  closure_function = outer_function(first_number)
  # Call the closure with second_number
  result = closure_function(second_number)
  print(result)  # Output: the outer function captured 5 and the inner function received 10, and their sum is 15
  return

if __name__ == "__main__":
  main()
