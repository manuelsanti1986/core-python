# Welcome to Manuel's Python Fundamentals Repository

## Core Python: Getting Started
### *by Rober Smallshire and Austin* Bingham

---

## Description

The following repository contains the projects prepared by **Manuel Santiago**.

---

## Configuration

### Ubuntu

#### 1. Python version

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
  
- Make sure the `apt_pkg.so` exists inside the python `dist-packages/` directory:
  - `cd /usr/lib/python3/dist-packages`
  - `ls -l`
  - If the `apt_pkg.so` does not exist:
    - `sudo apt-get install python3-apt --reinstall`
    - `sudo ln -s apt_pkg.cpython-36m-x86_64-linux-gnu.so apt_pkg.so`
    - Make sure the file was created, if it is not, try finding the correct `apt_pkg.python...` file

#### 2. Executable Modules
  - To make a python module executable by the user:
    - `chmod +x module_name.py`

---

## Project Solutions
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

### Module 2: Objects, Types, and Collections

- **Concepts Overview:**
  - Python Object model
  - Named references to objects
  - Value vs. identity equality
  - Passing arguments and returning values
  - Python's type system
  - Scopes to limit name access
  - "EVERYTHING IS AN OBJECT"
  - Tu

- **Key Takeaways:**
  - References to objects are copied, not the object themselves.
  - Always use immutable objects for default values.
  - Dynamic typing
      - The type of an object reference is not resolved until the program is running
  - Python will not generally perform implicit conversion between types. The only exception is the conversion of if and while loop predicates to bool. 
  - Scopes in Python do not correspond to source code blocks.

---

### Resources:
- [Core Python: Getting Started by Rober Smallshire and Austin Bingham](https://app.pluralsight.com/library/courses/getting-started-python-core)

---

### Useful Links
- [Absolute vs Relative Module Imports](https://realpython.com/absolute-vs-relative-python-imports/)

---

### Contact Information
- [Manuel Santiago LinkedIn](https://www.linkedin.com/in/manuelesantiagolaboy/)

