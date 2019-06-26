# define empty books_tuple
books_tuple = ()

# convert books_tuple as a list
books_list = list(books_tuple)

# append new books item in the list
books_list.append('Business Theory')
books_list.append('Python Crash Course')
books_list.append('Instant MBA')
books_list.append('The Adventure of Doraemon and Nobita')

# reconvert books_list as an original books_tuple
convert_books_tuple = tuple(books_list)

# make a list
for books in convert_books_tuple:
    print(books)

print(books_tuple)
print(books_list)
print(convert_books_tuple)