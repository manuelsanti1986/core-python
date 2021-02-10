#! /usr/bin/env python3
import sys
from pprint import pprint as pp

import mod01_modularity.words as words
import mod02_objects_types_collections.objects as objects
import mod02_objects_types_collections.collections as collections
import mod04_iteration_iterables.iterations as iterations

from mod05_classes.Aircraft import Aircraft
from mod05_classes.Flight import Flight

from mod02_objects_types_collections.objects import main_objects




print('main.py __name__ : ')
print(__name__)

if __name__ == '__main__':
    ## Modularity
    print(objects.add_divider('Module 01 - Modularity'))
    url = sys.argv[1]
    print(url)
    words.main_words(url)

    ## Objects and Types
    print(objects.add_divider('Module 02 - Objects, Types, and Collections'))
    main_objects()
    print(dir(collections))
    print(collections.__name__)

    ## Collections
    collections.tuples_intro()
    collections.tuples_destructuring()
    collections.tuples_constructor()
    collections.string_methods()

    ## Iterations & Iterables
    print(objects.add_divider('Module 04 - Iterations & Iterables'))
    iterations.list_comprehensions()
    iterations.set_comprehensions()
    iterations.dict_comprehensions()
    iterations.filtering_comprehensions()
    iterations.generator_functions()
    iterations.state_in_generators()
    iterations.generator_expressions()
    iterations.iteration_tools()

    ## Classes
    print(objects.add_divider('Module 05 - Classes'))
    aircraft01 = Aircraft('G-EUPT', 'Airbus A319', 10, 6)
    flight01 = Flight('BA758', aircraft01)
    pp(flight01.get_seating())

    flight01.allocate_seat_specific('5B', 'Tomatito')
    flight01.allocate_seat_specific('5A', 'Cebollita')
    flight01.allocate_seat_specific('5C', 'Pepinillo')
    pp(flight01.get_seating())




