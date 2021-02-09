def add_divider(title):
    divider = '\n' + '-' * len(title) + '\n'
    divider += title + '\n'
    divider += '-' * len(title)
    return divider

def replace_contents(g):
    g[0] = 7
    g[1] = 8
    g[2] = 9
    g[3] = None
    print('g: ', g)

def replace(g):
    g = [5, 6, 7] # Reassigning reference to a new list, so it is a new list
    print('g: ', g)

# Function arguments are transferred using pass-by-object-reference.
# References to objects are copied, not the object themselves.
def modify(k):
    k = k
    k.append(39)
    print('k: ', k)


def main_objects():
    m = [1, 2, 3]
    modify(m)
    print('m: ', m)
    replace(m)
    print('m: ', m)
    replace_contents(m)
    print('m: ', m)
