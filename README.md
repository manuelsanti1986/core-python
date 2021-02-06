# Welcome to Manuel's Python Fundamentals Repository

## Core Python: Getting Started
### *by Rober Smallshire and Austin* Bingham

---

## Description:

The following repository contains the projects prepared by **Manuel E. Santiago Laboy**.

---

## Configuration:

### Ubuntu: 

#### 1. Python version:

- From the terminal, confirm python version is the latest (3.8 at the moment)
  - `python --version`
  
- If the version is not the latest, make sure to install the latest version.
  - `sudo apt-get install software-properties-common`
  - `sudo apt-get install python3.8`
  
- Configure the alternatives to ensure the `python` and `python3` commands use the latest version: 
  - Add the installed version as an alternative
    - `sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 3`
    - `sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 4`
  - Make sure the default alternative is the latest version:
    - `sudo update-alternatives --config python`
      - Select option 0, it should be set to use `/usr/bin/python3`
    - `sudo update-alternatives --config python3`
      - Select option 0, it should be set to use `/usr/bin/python3.8`

#### 2. Executable Modules:
  - To make a python module executable by the user:
    - `chmod +x module_name.py`

---

## Assignment Solutions:
### Module 1: Modularity

- **Concepts Overview:**
    - Reusable Functions
    - Source code files called modules
    - Modules can be used from other modules
    - Importing modules
    - Programs or scripts
    - Python execution model
    - Make programs executable
    - Using docstrings to document functions, modules, and classes 


---

### Resources:
- [Core Python: Getting Started by Rober Smallshire and Austin Bingham](https://app.pluralsight.com/library/courses/getting-started-python-core)

---

### Useful Links
- [Absolute vs Relative Module Imports](https://realpython.com/absolute-vs-relative-python-imports/)


