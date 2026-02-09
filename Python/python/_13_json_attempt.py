#7/8/25
# 1. Import the built-in json library
import json

# 2. Store your JSON data in a multi-line string.
#    You would typically load this from a file, but this is a good first step.
json_data = """
[
    {
        "name":"Hersy",
        "lastaname":"Helston",
        "age": 18,
        "friends": ["Craice", "Ashley", "Misery", "Sthephany"]
    },
    {
        "name":"Craice",
        "lastaname":"Mailer",
        "age": 19,
        "friends": ["Hersy", "Ashley", "Misery", "Sthephany"]
    }
]
"""

# 3. Use json.loads() to convert the JSON string into Python objects
people = json.loads(json_data)

# 4. Now 'people' is a regular Python list of dictionaries.
#    You can access the data just like any other list or dictionary!
print(f"The type of 'people' is: {type(people)}")
print(f"The number of people in the list is: {len(people)}\n")

# Let's print some info from the first person in the list
first_person = people[0]
print(f"First person's name: {first_person['name']}")
print(f"First person's age: {first_person['age']}")
print(f"First person's friends: {first_person['friends']}\n")

# We can also loop through the list to access each person
print("--- Looping through the data ---")
for person in people:
    name = person["name"]
    friends = person["friends"]
    print(f"{name} is friends with: {', '.join(friends)}")

####

# The file name is `my_first_json.json`
file_name = "my_first_json.json"

# Use a 'with' statement to open the file.
# This is the safest way to handle files in Python.
try:
    with open(file_name, 'r') as file:
        # json.load() reads the entire file and converts the content
        # into a Python object (in this case, a list of dictionaries).
        people = json.load(file)

    # Now you have the data in the 'people' variable.
    print(f"Successfully loaded data from '{file_name}'.")
    print(f"Number of people: {len(people)}")

    # You can now access the data just like before.
    print(f"First person's name is: {people[0]['name']}")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except json.JSONDecodeError:
    print(f"Error: The file '{file_name}' does not contain valid JSON.")


numbs=[1,2,3,5]
print(max(numbs))


