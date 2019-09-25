# Functions
def make_dough(argument_1, argument_2):
    if argument_1.lower() == "wheat" or argument_2.lower() == 'water':
        return 'dough'
    elif argument_2.lower() == "wheat" or argument_1.lower() == 'water':
        return 'dough'
    else:
        return 'not dough'

def wood_oven(argument_1):
    if argument_1.lower() == 'dough':
        return 'Naan'
    else:
        return 'not Naan'


# Calling of functions

# Tests TDD

# As a user I can pass 'wheat' and 'water' to the function make_dough, so that I can make 'dough'.
print('Testing make_dough, with "wheat" and "water" --> "dough" to be outputted')
print(make_dough('wheat', 'water') == 'dough')

# As a user I can pass things that are not 'wheat' and 'sand' to the function make_dough, and not make dough
print('Testing make_dough, with "sand" & "cement" --> "not dough" to be outputted')
print(make_dough('sand', 'cement') == 'not dough')

# As a user I can pass 'dough' to the function wood_oven, so that I can make Naan.
print('Testing wood_oven, with "dough" --> "Naan" to be outputted')
print(wood_oven('dough') == 'Naan')

# As a user I can pass things that are not 'dough' to the function wood_oven, and not make Naan.
print('Testing wood_oven, with "tortillas" --> "not Naan" to be outputted')
print(wood_oven('tortillas') == 'not Naan')

