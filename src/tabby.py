"""
Tabby is a ruff'n'ready printer for tabular data. Given data,
it'll format it into a table for you

An example call could be

    names = ["Joe", "Sarah", "Jim", "Alice"]
    ages  = [25, 32]
    job   = ['Software Developer', 'Baker', 'Mechanical Engineer', 'Unemployed']
    dob   = [1990, 1994, 1987, 1834]
    height = ["5'6", '5 foot', '6 foot 3 inches']

    tabby_print(names, ages, job, dob, height, headings=['name', 'ages', 'occupation','dob', 'height'])

tabby_print takes an arbitrary amount of data and also an array of headings
if you like.

Note that the arrays passed in do not have to be equal length, any empty
values will be filled with a null value

Beware:
"""

import itertools

def tabby_print(*arrays, **kwargs):
    """Prints our data in a tabular format
    example
        tabby_print(
            [1,2,3,4],
            ['joe','jim','jon','jak'],
            headings=['id', 'name']
        )
    outputs

        |id |name    
        +----------+    
        |1  |joe     
        +----------+ 
        |2  |jim     
        +----------+ 
        |3  |jon     
        +----------+ 
        |4  |jak     
        +----------+ 
    """    
    zipped = itertools.zip_longest(*arrays, fillvalue="nil")
    l = get_table_length(*arrays)
    divider = '+' + '-'*(l) + '+'

    for i, heading in enumerate(kwargs['headings']):
        l = get_column_length(i, itertools.zip_longest(*arrays, fillvalue='nil'))
        print('|' + str(heading) + (' ' * (l - len(str(heading)))), end="")
        #If we're on our final item, add a newline'
        if i == len(kwargs['headings'])-1:
            print()
    for tuples in zipped:
        print(divider)
        for i, item in enumerate(tuples):
            l = get_column_length(i, itertools.zip_longest(*arrays, fillvalue='nil'))
            print('|' + str(item) + (' ' * (l - len(str(item)))) , end="")
        print()
    print(divider)

def get_table_length(*arrays):
    """Gets the sum of the max length of all columns
    so that we know how long our table should be. Also
    does +2 to the result so it looks nicer"""
    _sum = 0
    for i in range(len(arrays)):
        _sum += get_column_length(i, itertools.zip_longest(*arrays, fillvalue='nil'))
    return _sum + 2

def get_column_length(n, zipped):
    """Returns the length of the largest string in a column.
    This is used to space our tables nicely. We +2 to the length
    just so it looks a bit nicer"""
    zipped = list(zipped)
    column = [str(column[n]) for column in zipped]
    length = len(max(column, key=len))
    return length + 2
