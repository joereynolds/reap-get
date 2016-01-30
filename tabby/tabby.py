import itertools

"""Instead of using length like we do now, get the largest value for each
column. That'll look better and hog less screen space"""
def tabby_print(*arrays, **kwargs):
    """Prints it to the console"""
    zipped = itertools.zip_longest(*arrays, fillvalue="nil")
    length = max_all(*arrays)
    divider = '+' + '-'*(length * len(arrays)) + '+'

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

def max_all(*arrays):
    """Gets the max length from all arrays"""
    _max = 0
    for array in arrays:
        for item in array:
            if len(str(item)) > _max:
               _max = len(str(item))
    return _max

def get_column_length(n, zipped):
    """Returns the length of the largest string in a column.
    This is used to space our tables nicely. We +2 to the length
    just so it looks a bit nicer"""
    zipped = list(zipped)
    column = [str(column[n]) for column in zipped]
    length = len(max(column, key=len))
    return length + 2

def test():
    
    names = ["Joe", "Sarah", "Jim", "Alice", 'Melissa','Andrew']
    ages  = [25, 32, 45, 30]
    job   = ['Software Developer', 'Baker', 'Mechanical Engineer', 'Single Mother', 'Unemployed']
    dob   = [1990, 1994, 1987, 1834]

    tabby_print(names, ages, job, dob, headings=['name', 'ages', 'occupation','dob'])

test()    
