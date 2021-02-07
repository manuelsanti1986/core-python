# Welcome to Manuel's Python Fundamentals Repository

## Core Python: Getting Started
### *by Rober Smallshire and Austin Bingham*

---

## Description

The following repository contains the projects prepared by **Manuel Santiago** while following the *Core Python: Getting Started* training.

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
    - `sudo apt-get install python3-apt --reinstall` or `sudo apt-get install python-apt --reinstall` depending on the version
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

- **Key Takeaways:**
  - **References to objects are copied, not the object themselves.**
  - Always use immutable objects for default values.
  - Dynamic typing
      - The type of an object reference is not resolved until the program is running
  - Python will not generally perform implicit conversion between types. The only exception is the conversion of if and while loop predicates to bool. 
  - Scopes in Python do not correspond to source code blocks.
  - Use `str.join()` to join strings instead of `+`
  - Data Types:  
    - **Boolean**
    - **Numeric:**
      - **int:**
      - **float:**
      - **complex:**
    - **Binary:**
      - **byte:** Immutable sequences of single bytes.
      - **bytearray:** Mutable counterpart to bytes objects.
      - **memoryview:** Allow Python code to access the internal data of an object that supports the buffer protocol without copying.
    - **Collections:**
      - **List:** Ordered collection which is changeable. Items do not need to be the same data
      - **Tuples:** Immutable sequence of arbitrary objects.
      - **Range:** Arithmetic progression of integers
      - **Set:** Immutable collection of unique and immutable objects
      - **Dictionary:** Unordered collection of key-value pais
       type.
      - **String:** Sequence of unicode characters  

### Module 3: Exceptions

- **Concepts Overview:**
  - Exception concept
  - Raising Exceptions
  - Control flow
  - Catching Exceptions
  - Unhandled Exceptions
  - Built-in exceptions
  - Programmer vs user erros
  - Resource cleanup

- **Key Takeaways:**
  - Exceptions are a mechanism for interrupting normal program flow and continuing in surrounding context.
  - Use `str()` to convert exceptions to string
  - Generally, do not catch the *TypeError* exception
  - Implement platform-specific actions with *ImportError* and EAFP

### Module 4: Iteration and Iterables

- **Concepts Overview:**
  - Low-leve iterable API
  - Exceptions in iterations
  - The *yield* keyword
  - Statefulness, laziness, and infinite sequences
  - Generator Expressions
  - Iteration Tools

- **Key Takeaways:**
  - Test
  
---

### Resources:
- [Core Python: Getting Started by Rober Smallshire and Austin Bingham](https://app.pluralsight.com/library/courses/getting-started-python-core)

---

### Useful Links
- [Python Standard Library](https://docs.python.org/3/library/)
- [Python Standard Types](https://docs.python.org/3/library/stdtypes.html)
- [Absolute vs Relative Module Imports](https://realpython.com/absolute-vs-relative-python-imports/)

---

### Contact Information
- [Manuel Santiago LinkedIn](https://www.linkedin.com/in/manuelesantiagolaboy/)

