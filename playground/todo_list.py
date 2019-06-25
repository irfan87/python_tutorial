# a simple todo which implement the basic of CRUD
# no database involved in this project
# just for fun and test my skills and knowledge in Python

# define the todo_items as an empty array
todos = []

# add new item
todos.insert(0, 'get the car done')
todos.insert(1, 'fetch the kids at the school')
todos.insert(2, 'learn python')
todos.insert(3, 'listen to the blackpink song')

print("\nOriginal Todos")
# show the original todos list
for todo in list(todos):
    print(todo)
    
# append another new todos on the array
todos.append('watch movies')
todos.append('guitar session')

print("\nUpdated Todos")

# show the updated todos list
for todo in list(todos):
    print(todo)

# delete the certain list
del(todos[0])

todos.sort()

print("\nAfter remove")
for todo in list(todos):
    sorted(todo)
    print(todo)

# show the todo's item that I really wanted to do
print("\nPending todo")
for todo in todos[1:2]:
    print(todo)

todos_length = len(todos)
print(f"\nTodos Size: {todos_length}")

print(todos)