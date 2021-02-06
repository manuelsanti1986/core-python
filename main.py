#! /usr/bin/env python3
import sys

import mod01_modularity.words as words
from mod02_objects_types.objects import main_objects




print('main.py __name__ : ')
print(__name__)

if __name__ == '__main__':
    url = sys.argv[1]
    print(url)
    words.main_words(url)
    main_objects()
    print(dir(words))
    print(words.__name__)
