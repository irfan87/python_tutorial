# import printing_function
# from printing_function import print_models
# from printing_function import show_completed_models
# from printing_function import print_models as pm
# from printing_function import show_completed_models as complete_models
# import printing_function as printing
from printing_function import *

# start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)