def print_models(unprinted_designs, completed_models):
    # simulate printing each design, until none are left
    # move each design to completed_models after printing
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    # display all completed models
    print("\nThe following models have been printed: ")

    for index, completed_model in enumerate(completed_models, start=1):
        print(f"{index}. {completed_model}")


# start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)