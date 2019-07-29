from collections import OrderedDict

glossary = OrderedDict()

glossary['string'] = 'A series of characters'
glossary['comment'] = 'A note in a program'
glossary['list'] = 'A collection of items in a particular order'
glossary['loop'] = 'Work through a collection of items, one at a time'
glossary['dictionary'] = 'A collection of key-value pairs'

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")