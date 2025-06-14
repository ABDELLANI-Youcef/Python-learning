"""
This is the main entry point for the fruits shop application.
"""
from pathlib import Path
import csv

def create_csv(path, fruits, total_cost, tip, grand_total):
  """
  Create a CSV file with the fruit orders and totals.
  """
  with path.open('w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Fruit Name', 'Price'])
    writer.writerows(fruits)
    writer.writerow(['Total Cost', total_cost])
    writer.writerow(['Tip', tip])
    writer.writerow(['Grand Total', grand_total])

    print(f"The fruits shop has been created and saved to {path}")

def calculate_totals(fruits):
  total_cost = sum(price for _, price in fruits)
  tip = total_cost * 0.2  # Assuming a 15% tip
  grand_total = total_cost + tip
  return total_cost, tip, grand_total

def serve_user():
  fruits = []
  while True:
    name = input("Enter the fruit name of (or 'f' to finish):")
    if name.lower() == 'f':
      break
    try:
      price = float(input(f"Enter the price for {name}: "))
    except ValueError:
      print("Invalid price. Please enter a valid number.")
      continue
    fruits.append((name, price))
  return fruits

def main():
  # get table number from user
  try:
    table_no = int(input("Enter your table number: "))
    print(f"Starting a tab for table {table_no}")
  except ValueError:
    print("Invalid input. Please enter a valid table number.")
    return


  # create file path using table number
  path = Path(__file__).parent / f"table_{table_no}.csv"
  print(path)

  # get items from user (fruit name and price)
  fuits = serve_user()
  print(f"Fruits ordered: {fuits}")

  # calculate the totals (total, tip, grand total)

  if not fuits:
    print("No fruits ordered. Exiting.")
    return

  total_cost, tip, grand_total = calculate_totals(fuits)
  print(f"Total cost: {total_cost:.2f}, Tip: {tip:.2f}, Grand Total: {grand_total:.2f}")

  # create the  csv
  create_csv(path, fuits, total_cost, tip, grand_total)
  return


if __name__ == "__main__":
  main()