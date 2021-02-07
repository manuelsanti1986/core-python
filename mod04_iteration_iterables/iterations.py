def list_comprehensions():
    str = 'Hola mis amigos'
    words = str.split(' ')
    lengths = []
    for word in words:
        lengths.append(len(word))
    print(str)
    print(lengths)
