import math

def minmax(sequence):
    return min(sequence), max(sequence)

def tuples_intro():
    tuple_test = (0,)
    print(tuple_test, end=': ')
    print(type(tuple_test))
    tuple_test = (0, 1, 2, 3)
    print(tuple_test, end=': ')
    print(type(tuple_test))
    tuple_test = 4, 5, 6, 7
    print(tuple_test, end=': ')
    print(type(tuple_test))
    tuple_test = (0, 'string', 3)
    print(tuple_test, end=': ')
    print(type(tuple_test))
    tuple_test = minmax([0, 2, 3, 66, 92, -4])
    print(tuple_test, end=': ')
    print(type(tuple_test))

def tuples_destructuring():
    (a, b, (c, d), f) = (0, 2, ('string', 2.3), 5)
    print('a:', a, '; b:', b, '; c:', c, '; d:', d, '; f:', f)
    a = 'first'
    b = 'second'
    print('a:', a, '; b:', b)
    a, b = b, a
    print('a:', a, '; b:', b)

def tuples_constructor():
    tuple_test = tuple([3, 555, 983, 444])
    print(tuple_test, end=': ')
    print(type(tuple_test))
    tuple_test = tuple("Hola")
    print(tuple_test, end=': ')
    print(type(tuple_test))
    collection_contains('H', tuple_test)
    collection_not_contains('j', tuple_test)

def string_methods():
    str = ';'.join(['1', '2', '3'])
    print(str)
    str =''.join(['ho', 'la'])
    print(str)
    str = str.split(';')
    print(str)
    str = 'unforgetable'.partition('forget')
    print(str)
    str =''.join(str)
    print(str)
    str = "{0} north, {1} east".format(45.89, 14.9)
    print(str)
    str = "{lat} north, {lon} east".format(lat=33.9, lon=71.9)
    print(str)
    str = "x= {pos[0]}, y= {pos[1]}".format(pos=[35, 21])
    print(str)
    str = "pi= {m.pi}, euler= {m.e}".format(m=math)
    print(str)


def collection_contains(value, collection):
    isInside = value in collection
    print(isInside)

def collection_not_contains(value, collection):
    isInside = value not in collection
    print(isInside)


