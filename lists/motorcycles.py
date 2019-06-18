motorcycles = []

# append the list of the motorcycles to the end
motorcycles.append('ducati')
motorcycles.append('honda')
motorcycles.append('suzuki')

# insert new motorcycle on the array list
motorcycles.insert(0, 'lambaretta')

# remove the unwanted motorcycle
del motorcycles[3]

message = f"I really want to have {motorcycles[0].title()} in my garage!"

print(motorcycles)
print(message)