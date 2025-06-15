# CHALLENGE: Shopping list formatter

shopping_list = []

# SECTION ONE - creating the shopping list
while True:
  item = input("Enter an item (or 'q' to quit): ")
  if item == 'q':
    break

  # Challenge: ask user for price (int)
  # handle any ValueError by printing a message, skipping a loop and asking for a new item
  while True:
    try:
        price = int(input("Enter the price (£) of the item: "))
        shopping_list.append((item, price))
        break
    except ValueError as e:
      print("the value you antered is not a valid price. Please enter a valid integer.")
      print(e)

# SECTION TWO - formatting the shopping list
total = 0
for i in shopping_list:
  print(f"{i[0]} costs {i[1]}£")
  total += i[1]

# we can use another way :===> for item, print in shopping_list

print("\n\n")
for item, price in shopping_list:
  print(f"{item} costs {price}£")
# Challenge: use a for loop to print each item and price on its own
print(f"the total price it {total}£")