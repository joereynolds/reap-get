import itertools

"""Instead of using length like we do now, get the largest value for each
column. That'll look better and hog less screen space"""
def tabby_print(*arrays, **kwargs):
    """Prints it to the console"""
    zipped = itertools.zip_longest(*arrays, fillvalue="nil")
    length = max_all(*arrays)
    divider = '+' + '-'*(length * len(arrays)) + '+'

    for i, heading in enumerate(kwargs['headings']):
        print('|' + str(heading) + (' ' * (length - len(str(heading)))), end="")
        #If we're on our final item, add a newline'
        if i == len(kwargs['headings'])-1:
            print()
    for i, tuples in enumerate(zipped):
        print(divider)
        for item in tuples:
            print('|' + str(item) + (' ' * (length - len(str(item)))) , end="")
        print()
    print(divider)

def max_all(*arrays):
    """Gets the max length from all arrays"""

    #could probably use map or something here but here we are...
    _max = 0
    for array in arrays:
        for item in array:
            if len(str(item)) > _max:
               _max = len(str(item))
    return _max

def test():
    
    names = ["Joe", "Sarah", "Jim", "Alice", 'Melissa','Andrew']
    ages  = [25, 32, 45, 30]
    job   = ['Software Developer', 'Baker', 'Mechanical Engineer', 'Single Mother', 'Unemployed']
    dob   = [1990, 1994, 1987, 1834]

    tabby_print(names, ages, job, dob, headings=['name', 'ages', 'occupation','dob'])

test()    
