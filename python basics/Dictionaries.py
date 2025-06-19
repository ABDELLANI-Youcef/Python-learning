# dictionaries

person = {
  "name": "John",
  "age": 30,
  "job": "Engineer",
  "Height": 5.4,
  "is_student": False,
  "skills": ["Python", "Java", "C++"],
  "address": {
    "city": "New York",
    "zip_code": "10001"
  },
  (1, 2): "Coordinates"
}

print(f"Person: {person}\n----------------------------------------------------------------------\n\n\n")

# methods
print("Length of person dictionary:", len(person))
print(person.get("name"))  # Accessing value using key
print("Is 'age' key in person?", "age" in person)
print("Is 'salary' key in person?", "salary" in person)  # Key not present
print("Keys:", person.keys())
print("Values:", person.values())
print("Items:", person.items())
print("Name:", person["name"])
print("Age:", person.get("age"))
print("Job:", person.get("job", "Not specified"))  # Default value if key not found

copied_person = person.copy()  # Copying the dictionary
print("Copied person:", copied_person)

person.update({"salary": 50000, "address": 7})  # Adding a new key-value pair
print("Updated person:", person)
person.pop("is_student")  # Removing a key-value pair
print("Person after removing 'is_student':", person)

person.clear()  # Clearing the dictionary
print("Person after clearing:", person)