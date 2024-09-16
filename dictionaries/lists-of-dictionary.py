# Print out - the name, job and city of each employee using a loop. The program must work for any number of employees in the list, not just 2
employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]

for employee in employees:
    print(f"Name: {employee['name']}")
    print(f"Job: {employee['job']}")
    print(f"City: {employee['address']['city']}")
    print("-----------------------")

# Prints the country of the second employee in the list by accessing it directly without the loop.
employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]

country = employees[1]["address"]["country"]
print(f"country of second employee: {country}")