# Documentation  

## Notes on the web
https://ncar.github.io/python-tutorial/

## Videos on youtube
https://www.youtube.com/channel/UCoZPBqJal5uKpO8ZiwzavCw

-------------------------------------------------------

# Virtual environment 

## create virtual environment for this project:
>*conda create --name python_tutorial python*

## activate the virtual environment
>*conda activate python_tutorial*

## List available environment
>*conda env list*

-------------------------------------------------------

# Git instructions

## Local repo
>*git init .*
>
>*git status*
>
>*git add file.txt*
> 
> *git add -A* or *git stage -A* 
>
>*git commit -m "Adding sample data file"*
>
>*git log* or *git log --oneline*
>
>*git mv file1 file2*

## Remote repo
Create a new repo on the github page. Copy link to this repo: git@github.com:cecilehannay/python_tutorial.git

Push an existing repository from the command line
>*git remote add origin git@github.com:cecilehannay/python_tutorial.git*
>
>*git remote -v*
>
>*git branch -M main*
>
>*git push -u origin main*
>

### Adding .gitignore 
Include file we don't want to include like  \__pycache__\

>* git add .gitignore*
>
>* git commit -m "Ignoring pycache"*

-------------------------------------------------------

# Creating package

A package is a directory containing a file called \__init__.py\ inside it. (Note that this file is commonly empty.)

Create a new directory called mysci and create an empty file in it called \__init__.py\

>*mkdir utils*
>
>*cd utils*
>
>*touch \__init__.py\*
>
>*cd ..*

Then, move the 3 modules into this package:
>*git mv readdata.py myutils/*
>
>*git mv printing.py myutils/*
>
>*git mv computation.py myutils/*


Then, let’s modify the import statements:
>*from myutils.readdata import read_data*
>
>*from myutils.printing import print_comparison*
>
>*from myutils.computation import compute_heatindex*

Stage everything (don’t forget the \__init__.py\ file!) and commit
>*git add -A*
>
>*git commit -m "Creating myutils package"*

Create a setup.py file one level above your myutils package (in the python_tutorial directory):
The setup.py file is a Python file necessary for package distribution. This file tells pip how to install your package into the common Python space for your python interpreter. Required information is the name of your package, the version of your package (which you can choose), and a list of packages you’d like installed by pip (e.g., your mysci package).

>*touch setup.py*

Edit setup.py

*
from setuptools import setup

setup(
    name="myutils",
    version="1.0.0",
    description="myutils package",
    author="Cecile Hannay",
    author_email="hannay@ucar.edu",
    packages=["myutils"],
    install_requires=[],
)
*


Push to GitHub!

>*git add setup.py*
>
>*git commit -m "Adding setup.py"*
>
>*git push origin main*

Pip Install your package locally.
To test that our package is set up correctly, let’s install it into our project repository.

>* pip install . *

Everything should install smoothly, and now you will be able to import mysci in any Python code that you write, regardless of where that code is…*as long as you use the same python interpreter*! See the Note below.

Let’s use pip to uninstall the package we just installed:

>*pip uninstall myutils*

Install from your GitHub repository
Now, let’s re-install our package directly from GitHub.

>* pip install git+https://github.com/cecilehannay/python_tutorial.git *

Show which package are install
>*conda list*