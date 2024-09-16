from user import User

app_user_one = User("chinu@nn.com", "Chinmaya", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

app_user_one.change_job_title("DevOps Trainer")
app_user_one.get_user_info()

app_user_two = User("pallavi@sai.com", "Sai Pallavi", "Pallavi1", "Doctor")
app_user_two.get_user_info()
