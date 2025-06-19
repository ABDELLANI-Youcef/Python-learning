is_great = True

print("is_great", is_great)
print("!is_great", not is_great)
print("is_great and not is_great", is_great and not is_great)
print("is_great or not is_great", is_great or not is_great)
print("type(is_great)", type(is_great))

# comparison = 5 > 3
x, y = 5, 30
print("x > y", x > y)  # False
print("x < y", x < y)  # True
print("x >= y ====>", x >= y)  # False
print("x <= y ====>", x <= y)  # True
print("x == y ====>", x == y)  # False
print("x != y ====>", x != y)  # True

if 1: print("1 is truthy")
if not 0: print("0 is falsy")
if "": print("Empty string is falsy")
if "Hello": print("Non-empty string is truthy")
if []: print("Empty list is falsy")
if [1, 2, 3]: print("Non-empty list is truthy")
if {}: print("Empty dictionary is falsy")
if {"key": "value"}: print("Non-empty dictionary is truthy")
if None: print("None is falsy")
if not None: print("None is falsy")
if True: print("True is truthy")
if False: print("False is falsy")

# conditionnal

age = int(input("Enter your age please: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Ternary operator
is_adult = "You are an adult." if age >= 18 else "You are a minor."
print(is_adult)

if age >= 18 and age < 65:
    print("You are an adult.")
elif age >= 65:
    print("You are a senior citizen.")
else:
    print("You are a minor.")

if age < 18 or age >= 65:
    print("You are either a minor or a senior citizen.")

if age < 18 is True:
    print("You are a minor.")
elif age >= 65 is not True:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# ternary operator with multiple conditions
is_adult = "You are an adult." if age >= 18 else "You are a minor."
print(is_adult)
# Using the ternary operator with multiple conditions
is_adult = "You are an adult." if age >= 18 else "You are a senior citizen." if age >= 65 else "You are a minor."
print(is_adult)
# Using the ternary operator with multiple conditions and logical operators
is_adult = "You are an adult." if age >= 18 and age < 65 else "You are a senior citizen." if age >= 65 else "You are a minor."
print(is_adult)