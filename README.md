# GitHub Automation

GitHub automation script made with Python using PyGithub. The script first creates repository on Github and then clones it to your system. After cloning it adds a readme file to the project and pushes it back to Github.

### Prerequisites

- PyGithub
  - Install by pip install PyGithub in your virtual enviroment
  
- Make sure Github is already set for your system

### Installing


- Step 1: Put the python script and bash files in their respective locations.
- Step 2: Add the bash files to bash.rc
          - Add source ~/mycmds.sh  to the end of bash.rc
- Step 3: Make sure the directories are correct for both the bash and python script
- Step 5: Change the username and password in python script
- Step 6: Run the script

## Problems you might face

You may face issues authenticating to github, make sure your are using SSH key.

