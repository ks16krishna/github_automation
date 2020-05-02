import os
from github import Github

# Define username and password for your Github Account
username = 'username'
password = 'password'

# Global Variables here

# Name of the repository you want to create
reponame = input('Name of the repo: ')

clone = 'git clone https://github.com/{}/{}.git'.format(username, reponame)

# Enter your own Project folder directory where you want to create your repository
mydir = "/home/krishna/Projects"


# Function to create repo on github
def create_rep():
    os.system("clear")
    user = Github(username, password).get_user()
    try:
        repo = user.create_repo(reponame)
    except:
        print("Error occurred try again")
        create_rep()


# Function to clone the repo on the system
def create_folder():
    os.chdir(mydir)
    try:
        print("Repo created successfully")
        os.system(clone)
        os.system("clear")
    except:
        # I think this is pretty much useless xD
        print("%s already exists" % reponame)
        create_rep()

    os.chdir(reponame)
    os.system("git init")
    os.system("touch README.md")
    os.system("git add README.md")
    os.system("git commit -m 'First commit'")
    os.system('git push -u origin master')
    os.system("echo Task completed successfully")


if __name__ == "__main__":
    create_rep()
    create_folder()
