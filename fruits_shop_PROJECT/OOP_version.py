import csv
from pathlib import Path

class FruitShop:
  def __init__(self, table_number):
    self.table_number = table_number
    self.fruits = []
    self.total = 0
    self.tip = 0
    self.grand_total = 0

  def serve_user(self):
    while True:
      name = input("Enter the fruit name of (or 'f' to finish):")
      if name.lower() == 'f':
        break
      try:
        price = float(input(f"Enter the price for {name}: "))
      except ValueError:
        print("Invalid price. Please enter a valid number.")
        continue
      self.fruits.append((name, price))

  def calculate_totals(self):
    self.total = sum(price for _, price in self.fruits)
    self.tip = self.total * 0.2  # Assuming a 15% tip
    self.grand_total = self.total + self.tip

  def create_csv(self):
    if not self.fruits:
      print("No fruits ordered. Exiting.")
      return
    path = Path(__file__).parent / f"table_{self.table_number}.csv"
    with path.open('w', newline='') as file:
      writer = csv.writer(file)

      writer.writerow(['Fruit Name', 'Price'])
      writer.writerows(self.fruits)
      writer.writerow(['Total Cost', self.total])
      writer.writerow(['Tip', self.tip])
      writer.writerow(['Grand Total', self.grand_total])


def main():
  shop = FruitShop(99)
  print(f"Starting a tab for table {shop.table_number}")
  shop.serve_user()
  print(f"Fruits ordered: {shop.fruits}")
  shop.calculate_totals()
  shop.create_csv()
  return

if __name__ == "__main__":
  main()