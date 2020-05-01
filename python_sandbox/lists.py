# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create lits
# numbers = [1, 2, 3, 4, 5]

# Using a constructor
numbers = list((1, 2, 3, 4, 5))
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']


# print(type(numbers))
# print(numbers)

print(fruits)

# Get Value
print(fruits[1])

# Get len
print(len(fruits))

# Append to list
fruits.append('Mangos')
print(fruits)

# Remove from list
fruits.remove('Grapes')
print(fruits)

# Insert into position
fruits.insert(2, 'Strawberry')
print(fruits)

# Remove from position
fruits.pop(3)
print(fruits)

# Reverse list
fruits.reverse()
print(fruits)

# Sort list
fruits.sort()
print(fruits)

# Reverse sort
fruits.sort(reverse=True)
print(fruits)