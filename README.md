# Documentation  

## Notes on the web
https://ncar.github.io/python-tutorial/

## Videos on youtube
https://www.youtube.com/channel/UCoZPBqJal5uKpO8ZiwzavCw


# Virtual environment 

## create virtual environment for this project:
>*conda create --name python_tutorial python*

## activate the virtual environment
>*conda activate python_tutorial*

## List available environment
>*conda envs list*


# Git instructions

## Local repo
>*git init .*
>*git status*
git add file.txt
git commit -m "Adding sample data file"
git log
git log --oneline
git mv file1 file2

## Remote repo
Create a new repo on the github page. Copy link to this repo: https://github.com/<user_name>/<repo>.git

push an existing repository from the command line
git remote add origin git@github.com:cecilehannay/tutorials.git
git remote -v
git branch -M main
git push -u origin main
