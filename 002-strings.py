print('Hello world')

a_plus_b = 'a' + 'b'
a_b_multiply_4 = 'ab' * 4
# a_minus_b = 'a' - 'b'  *error

print('a' + 'b')
print('ab' * 4)
# print(a_minus_b)

# escaping
mystring = 'It\'s an escaped quote!'
print(mystring)

mystring = "I'm a so-called \"script kiddie\""
print(mystring)

# Multiline
print("""Line 1,
Line 2,
Line 3""")

print('This is line 1,\nthis is line 2,\nthis is line 3.')
print('------------------------')
print('This is line 1,\rthis is line 2,')
print('------------------------')
print('This is line 1,\tthis is line 2,')

# String Operations
mystring = "olá, Mundo"
mystring2 = "OlaMundo"
mynum = 2
# list = ['apple', 'banana', 'cherry', 'cherry']
txt_expandtabs = "H\te\tl\tl\to"
txt_format = "For only {price:.2f} dollars!"
point = {'x':4,'y':-5}


mystring.capitalize() # Olá mundo 
mystring.casefold() # olá mundo
mystring.center(50) #                    olá mundo                   
mystring.count('o') # 1
mystring.encode() # b'Ol\xc3\xa1, Mundo'
mystring.endswith("o") # true
txt_expandtabs.expandtabs(4) # H   e   l   l   o
mystring.find('l') # 1
txt_format.format(price = 49) # For only 49.00 dollars!
'{x} {y}'.format(**point) # 4 -5
mystring.index('á') # 2

# length of string
len(mystring) # 10

# split string
mystring.split(' ') # ['olá,', 'Mundo']

# replace string
mystring.replace('á', '@') # ol@, Mundo
mystring.replace('o', '0') # 0lá, Mund0
mystring.replace('olá', 'Saudações') # Saudações, Mundo

# reverse string
mystring[::-1] # odnuM ,álo

# chaining calls
mystring.replace('Mundo', 'Terra').upper() # OLÁ, TERRA

#string formatting with f-strings
my_age = 40 # My age is 40
name = "John"
age = 56
f"{name=}, {age=}" # name='John', age=56

print(f"{name=}, {age=}")