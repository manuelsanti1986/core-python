#! /usr/bin/env python3
import sys

import mod01_modularity.words as words
import mod02_objects_types_collections.objects as objects
import mod02_objects_types_collections.collections as collections
import mod04_iteration_iterables.iterations as iterations

from mod02_objects_types_collections.objects import main_objects




print('main.py __name__ : ')
print(__name__)

if __name__ == '__main__':
    ## Modularity
    print(objects.add_divider('Module 01'))
    url = sys.argv[1]
    print(url)
    words.main_words(url)

    ## Objects and Types
    print(objects.add_divider('Module 02'))
    main_objects()
    print(dir(collections))
    print(collections.__name__)

    ## Collections
    collections.tuples_intro()
    collections.tuples_destructuring()
    collections.tuples_constructor()
    collections.string_methods()

    ## Iterations & Iterables
    print(objects.add_divider('Module 04'))
    iterations.list_comprehensions()
    iterations.set_comprehensions()
    iterations.dict_comprehensions()
    iterations.filtering_comprehensions()
    iterations.generator_functions()
    iterations.state_in_generators()
    iterations.generator_expressions()
    iterations.iteration_tools()



