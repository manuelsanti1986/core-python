#! /usr/bin/env python3
import sys

from mod01_modularity.words import main_words
from mod02_objects_types.objects import main_objects


print('main.py __name__ : ')
print(__name__)

if __name__ == '__main__':
    url = sys.argv[1]
    print(url)
    main_words(url)
    main_objects()
