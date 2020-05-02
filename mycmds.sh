 #!/bin/bash

function create() {
   #virtaul enviroment location
   source venv/bin/activate
   #the main python script location
   cd Projects/github_automation/   
   python3 main.py
}
