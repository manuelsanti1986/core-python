import os
import glob
from math import factorial, sqrt

def list_comprehensions():
    str = 'Hola mis amigos'
    words = str.split(' ')
    lengths = []
    for word in words:
        lengths.append(len(word))
    print(str)
    print(lengths)

def set_comprehensions():
    list_of_factorials = [len(str(factorial(x))) for x in range(0,20)]
    set_of_factorials = set(list_of_factorials)
    print(list_of_factorials)
    print(set_of_factorials)

def dict_comprehensions():
    country_to_capital = {
        'United Kingdom': 'London',
        'Morocco': 'Rabat',
        'Sweden': 'Stockholm',
        'Brazil': 'Brasilia'
    }
    capital_to_country = {capital: country for country, capital in country_to_capital.items()}
    print(country_to_capital)
    print(capital_to_country)
    file_sizes = {os.path.relpath(p): os.stat(p).st_size for p in glob.glob('*workplace/*')}
    print(file_sizes)

def is_prime(val):
    if(val < 2):
        return False
    for i in range(2, int(sqrt(val)) + 1):
        if val % i == 0:
            return False
    return True

def filtering_comprehensions():
    prime_numbers = [x for x in range(101) if is_prime(x)]
    print(prime_numbers)

