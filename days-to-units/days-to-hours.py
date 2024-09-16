calculation_to_units = 24
name_of_units = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered zero")
        else:
            print("you entered negative value")
    except ValueError:
        print("your input is not a valid number")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter number of days as a comma separated list and I will convert it to hours!\n")
    list_of_days = user_input.split(", ")
    print(list_of_days)
    print(set(list_of_days))
    print(type(set(list_of_days)))
    print(type(list_of_days))
    for num_of_days_element in set(list_of_days):
        validate_and_execute()
