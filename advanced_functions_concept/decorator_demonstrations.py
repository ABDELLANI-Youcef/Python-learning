"""
Decorators are a powerful feature in Python that allow you to modify the behavior of functions or methods.
They are often used for logging, access control, instrumentation, caching, and more.
They are similar to JavaScript decorators. they take a function as an argument and return a new function that adds some functionality to the original function.
Decorators can be applied to functions or methods using the @ syntax.
"""

def final_formal(func):
    """
    A decorator that modifies the behavior of the function it decorates.
    It adds a print statement before and after the function call.
    """
    def wrapper(*args, **kwargs):
        print("Before calling the function.")
        result = func(*args, **kwargs)
        print("After calling the function.")
        return result
    return wrapper

@final_formal
def modified_func():
  """
  This is a simple function that prints a message.
  It is used to demonstrate the use of decorators.
  """
  print("This is the original function.")

def main():
  """
  The main function that demonstrates the use of decorators.
  It calls the modified function and shows the output.
  """
  modified_func()
  # The output will show the print statements from the decorator
  # before and after the original function call.
  return 1

if __name__ == "__main__":
  main()