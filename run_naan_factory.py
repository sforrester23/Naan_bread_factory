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

def run_naan_factory(ingredient1, ingredient2):
    # is_dough = make_dough(ingredient1, ingredient2)
    # is_bread = wood_oven(is_dough)
    # return is_bread
    return wood_oven(make_dough(ingredient1, ingredient2))
print('/////////////')
print(run_naan_factory('wheat', 'water'))
print('/////////////')
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

# As a user, I should be able to pass wheat and water through make_dough and then wood_oven, to make naan bread!
# I.e. run the whole factory process
print('Testing run_naan_factory with "wheat" and "water" --> "Naan" to be outputted')
print(run_naan_factory('wheat', 'water')== 'Naan')

# As a user, I should be able to pass anything but wheat and water through make_dough and then wood_oven, to make naan bread!
# I.e. test the whole factory process
print('Testing run_naan_factory with "skunks" and "racoons" --> "not Naan" to be outputted')
print(run_naan_factory('skunks', 'racoons')== 'not Naan')