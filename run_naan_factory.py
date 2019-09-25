# Functions
def make_dough(argument_1, argument_2):
    return 'dough'

def wood_oven(agument_1):
    return 'Naan'


# Calling of functions

# Tests TDD

# As a user I can pass 'wheat' and 'water' to the function make_dough, so that I can make 'dough'.
print('Testing make_dough, with "wheat" and "water" --> "dough" to be outputted')
print(make_dough('wheat', 'water') == 'dough')

print('Testing make_dough, with "sand" & "cement" --> "not dough" to be outputted')
print(make_dough('wheat', 'water') == 'dough')

# As a user I can pass 'dough' to the function wood_oven, so that I can make Naan.
print('Testing wood_oven, with "dough" --> "Naan" to be outputted')
print(wood_oven('dough') == 'Naan')

