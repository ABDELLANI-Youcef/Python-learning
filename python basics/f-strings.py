name = "youcef"
score = 95
greeting = f"Hello {name}, your score is {score}."
print(greeting)
# Using f-strings to format strings
age = 30
height = 5.4
greeting_with_details = f"Hello {name}, you are {age} years old and {height} meters tall."
print(greeting_with_details)
# Using f-strings with expressions
print(f"{name.upper()} scored {score + 5} points in the exam.")

# old way to use formatted strings
greeting_old = "Hello {}, your score is {}.".format(name, score)
print(greeting_old)
# Using f-strings with dictionaries
person = {
    "name": "Youcef",
    "age": 30,
    "height": 5.4
}
greeting_dict = f"Hello {person['name']}, you are {person['age']} years old and {person['height']} meters tall."
print(greeting_dict)