# For-loop
for letter in 'Hello\n':
    print(letter) # Iterate word Hello and Print each letter

# For-loop lists
mylist = [1, 'a', 'Hello\n']

# Loop over list
for item in mylist:
    print(item) 

# print item un position 1 from list
print(mylist[1], '\n')

mylist = [1, 2, 'Hello', ['a', 'b'] ]
print(mylist[0]) # 1
print(mylist[0] + mylist[1]) # 3
print(mylist[2]) # Hello
print(mylist[3]) # ['a', 'b']
print(mylist[3][0]) # a

# While-loop
i = 0
while i <= 4:
    print(f"{i = }")
    i = i + 1
