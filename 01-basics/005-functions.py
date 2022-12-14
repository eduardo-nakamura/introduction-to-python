# print() Print argument to screen
print('Hello, readers!')

# len() returns the length of whatever you feed it
mylength = len('Hello')
print(mylength) # 5

# Creating functions
def say_hi(name):
    print('Hi', name)

say_hi('Naka') # Hi Naka

def welcome(name, location):
    print('Hi', name, 'welcome to', location)

welcome('Erik', 'this tutorial') # Hi Erik welcome to this tutorial

# Function return value
def add(a, b):
    return a + b

result = add(4, 8)
print(result) # 12

# Empty return statement
def optional_greeter(name):
    if name.startswith('X'):
        return

    print('Hi there, ', name)

optional_greeter('A-A Ron') # Hi there,  A-A Ron
optional_greeter('Xuxa') # 

# Variable Scope

def say_hi_scope():
    print("Hi", name)
    answer = "Hi"

name = 'Eirk'

# say_hi_scope() > Hi Eirk
# print(answer) > error name 'answer' is not defined

# Default values and named parameters
def welcome_default(name = 'learner', location = 'this tutorial'):
    print("Hi", name, "welcome to", location)

welcome_default() # Hi learner welcome to this tutorial
welcome_default(name='Naka') # Hi Naka welcome to this tutorial
welcome_default(location='Brazil') # Hi learner welcome to Brazil
welcome_default(name='Naka', location='Brazil') # Hi Naka welcome to Brazil
welcome_default('Erik', 'your home') # Hi Erik welcome to your home