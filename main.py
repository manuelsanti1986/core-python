#! /usr/bin/env python3
import sys

import mod01_modularity.words as words
import mod02_objects_types_collections.objects as objects
from mod02_objects_types_collections.objects import main_objects




print('main.py __name__ : ')
print(__name__)

if __name__ == '__main__':
    print(objects.add_divider('Module 01'))
    url = sys.argv[1]
    print(url)
    words.main_words(url)

    print(objects.add_divider('Module 02'))
    main_objects()
    print(dir(main_objects))
    print(main_objects.__name__)
