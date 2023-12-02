# Tuples - Collection that is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes')) Constructor method

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get value
# print(fruits[1])

# Delete tuple
# del fruits2

# Get length
# print(len(fruits))


# Set - Collection that is unordered and unindexed. No duplicate members
fruits_set = {'Apples', 'Oranges', 'Mangoes'}

# Check if in set
# print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Rm from set
fruits_set.remove('Grape')

# clear set
fruits_set.clear()

# delete set
del fruits_set

print(fruits_set)