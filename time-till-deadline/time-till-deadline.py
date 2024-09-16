
# 1. Create a program that allows a user to enter a goal and a deadline for that goal.
# 2. Calculate how many days from now that deadline is.
# 3. Print out how many days till the deadline.

from datetime import datetime

user_input = input("enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
time_till = deadline_date - today_date

hours_till = int(time_till.total_seconds() / 60 / 60)
print(f"Dear user! Time remaining for your goal: {goal} is {hours_till} hours")

