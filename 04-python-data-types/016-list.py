# creating a list
my_list = [1, 2, 3]
empty_list = []

my_list = [1, "Erik", { 'age': 39 }]
# list with three lists inside
game_board = [[], [], []]

# List function
list1 = list(range(1,4)) # [1, 2, 3]
list2 = list({1, 2, 2, 2, 3})  # [1, 2, 3]
list3 = list((1, 2, 3)) # [1, 2, 3]

# Accessing Python list elements by position
list1[1] # 2
list2[0] # 1

# last element
list2[-1] # Last Element (3)
list2[-2] # Second Last Element (2)

# NEsted Elements
nested_list = [[1,2],[3,4],[5,6]]
nested_list[0] # [1,2]
nested_list[0][0] # 1
nested_list[2][1] # 6

# Append to list
append_list = [1,2]
append_list.append('a') # [1, 2, 'a']
append_list.append(4) # [1, 2, 'a', 4]

# Combine or merge two lists

l1 = [1,2]
l2 = [3,4]
l3 = l1 + l2 # [1, 2, 3, 4]

l1.extend(l2) # [1, 2, 3, 4]

# Pop Items
pop_list = [1,2,3,4,5]
pop_list.pop() # 5
pop_list.pop() # 4
pop_list.pop(0) # 1
# pop_list [2, 3]

# Delete Items
delete_list = [1,2,3,4,5]
del(delete_list[0]) # delete 1
del(delete_list[2]) # delete 4
del(delete_list) # Delete list object

# Remove specific values from a Python list
remove_list = [1, 2, 3, 2, 5, 'awea']
remove_list.remove(2) 
#remove_list [1, 3, 2, 5, 'awea']
remove_list.remove('awea') 
#remove_list [1, 3, 2, 5]

# Clear List
clear_list = [1,2,3]
clear_list.clear() # []

# Remove duplicates from a list
duplicated_list = [1, 2, 2, 3, 5]
list(set(duplicated_list)) # a) convert to set to remove duplicates b) convert set back to list
# duplicated_list [1, 2, 3, 5]

#Replace items in a list
replace_list = [1,2,3,4,5]
replace_list[0] = 400
# replace_list [400, 2, 3, 4, 5]

# length
len(replace_list) # 5

#Counting element occurrence in a list
count_list = [1, 2, 1, 4, 1, 7]
my_list.count(1) # 3

#Check if an item is in a list
check_item_list = [1, 2]

if 1 in check_item_list:
    print("It's in the List")
else:
    print("It's not in the List")    

#Find the index of an item in a list
find_list = ['a', 'b', 'c','d','e', 'd' ]
find_list.index('d') # 3
print(find_list.index('d',4)) # 5

# iterate list
iterate_list = [1,2,3,4,5]
for n in iterate_list:
    print(n)

#Python list to string
str([1, 'abc', 2.3]) # "[1, 'abc', 2.3]"

#Sorting lists
# In-place list sort in ascending order
asc_list = [10, 2, 5, 4, 2]
asc_list.sort() # [2, 2, 4, 5, 10]

#In-place list sort in descending order
desc_list = [10, 2, 5, 4, 2]
desc_list.sort(reverse=True) # [10, 5, 4, 2, 2]

#Using sorted()
sorted_list = [10, 2, 5, 4, 2]
sorted(sorted_list) # [2, 2, 4, 5, 10]
sorted(sorted_list, reverse=True) # [10, 5, 4, 2, 2]

#Unsortable lists
my_mixed_list = [1, 'a', 2, 'B']
# my_mixed_list.sort() not supported between instances of 'str' and 'int'.

#Slicing

# my_list[start:stop:step]
# start is the first element position to include
# stop is exclusive, meaning that the element at position stop won’t be included.
# step is the step size. more on this later.
# start, stop, and step are all optional.
# Negative values can be used too.
slice_list = [1, 2, 3, 4, 5, 6, 7, 8]
slice_list[0:3] # get first three elements from position 0 [1, 2, 3]
slice_list[:3] # start is 0 by default [1, 2, 3]
slice_list[4:] # skip first 4 elements [5, 6, 7, 8]

#  step
#  1 by default
print(slice_list[::2]) # skip one each time [1, 3, 5, 7]

#Going backward
print(slice_list[::-1]) # -1 step to go backwards
print(slice_list[-2:-5:-1]) # -2: skip last item / -5: position start / -1: reverse

# Reversing Python lists
reverse_list = [1,2,3,4]
# In-place reverse
reverse_list.reverse()
print('Using list reverse:', reverse_list)
# Let's revert that...
reverse_list.reverse()

# Create a new, reversed list
reverse_list2 = reverse_list[::-1]
print('Reversed 2nd list: ', reverse_list2)

# Or use a reversed iterator
rev = reversed(reverse_list)
print('Reversed iterator: ', list(rev))

rev_slice=[1,2,3,4]
rev_slice[::-1] #[4,3,2,1]

# reverse iterator
lst_iterate = [1,2,3,4] 
rev_iterate = reversed(lst_iterate) # <list_reverseiterator object at 0x00000293878A3DF0>
for i in rev_iterate:
    print(i)