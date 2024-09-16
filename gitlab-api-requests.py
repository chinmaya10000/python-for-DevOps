import requests

response = requests.get("https://gitlab.com/api/v4/users/chinmaya10000/projects")
my_project = response.json()

for project in my_project:
    print(f"Project Name: {project['name']}\nProject Url: {project['web_url']}\n")


"""import requests

response = requests.get("https://api.github.com/users/chinmaya10000/repos")
my_project = response.json()

for repo in my_project:
    print(f"Project Name: {repo['name']}\nProject_url: {repo['html_url']}\n")"""

# pip install requests