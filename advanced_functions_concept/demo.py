import sys

def job_description(result, work, reason):

  return result(work, reason)

def success(work, reason):
  return f"the success in {work} is the result of {reason}"

def failure(work, reason):
  return f"the failure in {work} is the result of {reason}"

def main():
  print(f"I learned that {job_description(success, 'programming', 'hard work')}")

  fruits = ["apple", "banana", "cherry"]
  def command(fruit):
    return f"Eat {fruit}"

  orders = map(command, fruits)
  print(list(orders))

  numbers = [484, 6874 ,3546884 ,354]
  def bigger_than_1000(number):
    return number > 1000
  print("Numbers:", list(filter(bigger_than_1000, numbers)))
  return

if __name__ == "__main__":

  main()