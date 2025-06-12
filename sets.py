ingredients = {12, 57, 66, 57, 12}

print(ingredients)

ingredients.add(100)  # Adding an element
print("After adding 100:", ingredients)
ingredients.remove(57)  # Removing an element
print("After removing 57:", ingredients)
ingredients.discard(77 )  # Discarding an element (no error if not found)
print("After discarding 77 (not found):", ingredients)
ingredients.discard(66)  # Discarding an existing element
print("After discarding 66:", ingredients)

scores = set(["Python", "Java", "C++", "Python"])  # Creating a set with duplicates
tuple_set = set((1, 2, 3, 4))  # Creating a set from a tuple
print("Scores set:", scores)
print("Tuple set:", tuple_set)
# Set operations
joined = ingredients.union(scores)  # Union of two sets
print("Union of ingredients and scores:", ingredients, scores, ingredients.union(scores))

set_one = {1, 2, 3}
set_two = {3, 4, 5}
intersection = set_one.intersection(set_two)  # Intersection of two sets
print("Intersection of set_one and set_two:", intersection)
difference = set_one.difference(set_two)  # Difference of two sets
print("Difference of set_one and set_two:", difference)
symmetric_difference = set_one.symmetric_difference(set_two)  # Symmetric difference of two sets
print("Symmetric difference of set_one and set_two:", symmetric_difference)

# frozen set
frozen_ingredients = frozenset(ingredients)  # Creating a frozen set
print("Frozen ingredients:", frozen_ingredients)
# Attempting to add an element to a frozen set will raise an error

'''
try:
     frozen_ingredients.add(200) ======>  # This will raise an error
except AttributeError as e:
    print("Error:", e)
# Attempting to remove an element from a frozen set will also raise an error
try:
     frozen_ingredients.remove(12) =====> # This will raise an error
except AttributeError as e:
    print("Error:", e)
# Attempting to discard an element from a frozen set will also raise an error
try:
    frozen_ingredients.discard(12) ======>  # This will raise an error
except AttributeError as e:
    print("Error:", e)
# Attempting to create a frozen set from a mutable type will raise an error
'''