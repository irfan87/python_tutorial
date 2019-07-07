# set the deli menu as a lits
sandwich_orders = ['beef', 'chicken', 'tuna', 'eggs', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
        
    current_sandwich_order = sandwich_orders.pop()

    print(f"I made you a {current_sandwich_order} sandwich")

    finished_sandwiches.append(current_sandwich_order)

print("\nYour ordered sandwiches have been done: ")

for index, sandwich in enumerate(finished_sandwiches, start=1):
    print(f"{index}. {sandwich.title()} sandwich")