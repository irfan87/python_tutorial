glossary = {
    'number': 'a set of numbers',
    'float': 'a numerical value with a decimal component',
    'string': 'a set of characters',
    'dictionary': 'a collection of key-value pairs',
    'del': 'a built-in function to delete the items from the list permanently',
    'loop': 'work through a collection of items, one at a time',
    'comment': 'a note in a program that the Python interpreter ignores',
    'boolean expression': 'an expression that evaluates to True or False',
    'conditional test': 'a comparison between two values',
    'key': 'the first item in a key-value pair in a dictionary',
    'value': 'an item associated with a key in a dictionary',
}

for title, definition in glossary.items():
    if title == 'del':
        print(f"\n{title.lower()}: {definition}")
    else:
        print(f"\n{title.title()}: {definition}")