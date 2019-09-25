# Tests TDD

from naan_functions import *

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