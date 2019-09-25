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