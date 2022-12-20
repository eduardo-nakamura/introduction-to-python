# It can hold multiple values in a single variable
# It’s ordered: the order of items is preserved
# A tuple can have duplicate values
# It’s indexed: you can access items numerically
# A tuple can have an arbitrary length

# A tuple is immutable; it can not be changed once you have defined it.
# A tuple is defined using optional parentheses () instead of square brackets []
# Since a tuple is immutable, it can be hashed, and thus it can act as the key in a dictionary
my_numbers = (1, 2, 3)
the_same = 1, 2, 3
my_strings = ('Hello', 'World')
my_mixed_tuple = ('Hello', 123, True)

tuple_from_list = tuple([0,1,2,3]) # (0, 1, 2, 3)

# A tuple with just one item is useless for most use cases, but it demonstrates how Python recognizes a tuple: 
# because of the comma.

print((1)) # 1
print((1,)) # (1,)

# Multiple assignment
person = ('Erik', 38, True)
name, age, registered = person
print(name) # Erik

#Indexed access
print(person[1]) # 38

# Append to a Python Tuple
t1 = (1, 2, 3)
t2 = (*t1, 'Extra', 'Items')
print(t2) # (1, 2, 3, 'Extra', 'Items')

# Get tuple length

len(t1) # 3

# Convert Tuple to List
t = 1, 2, 3
list(t) # [1, 2, 3]

l = [*t, 4, 5, 6] 
print(l) # [1, 2, 3, 4, 5, 6]

# Convert tuple to set
s = set(t) # {1, 2, 3}
s = {*t} # {1, 2, 3}

# Convert tuple to string
str(t) # '(1, 2, 3)'