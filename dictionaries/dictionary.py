# Creating a dictionary
person = {
    'name': 'Chinmaya',
    'age': 22,
    'location': 'Bangalore',
    'skills': ['Python', 'DevOps', 'Kubernetes']
}

# Accessing dictionary values
print("Name:", person['name'])
print("Skills:", person['skills'])

# Adding a new key-value pair
person['Company'] = 'CrimsonLogic'
print("Updated Person:", person)

# Modifying an existing value
person['location'] = 'Hyderabad'
print("location:", person['location'])

# Removing a key-value pair using pop
person.pop('age')
print(person)

# Iterating over dictionary keys and values
for key, value in person.items():
    print(f"{key}: {value}")