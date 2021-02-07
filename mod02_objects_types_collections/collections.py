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

def collection_contains(value, collection):
    isInside = value in collection
    print(isInside)

def collection_not_contains(value, collection):
    isInside = value not in collection
    print(isInside)


