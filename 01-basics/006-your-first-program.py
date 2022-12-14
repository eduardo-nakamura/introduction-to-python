def say_hi(name):
    print("Hi there...")
    for letter in name:
        print(letter)
        

name = input("Your name: ") # ask for input and assign that input to a variable.

while name == '':
    print("You didn't enter your name!")
    name = input("Your name: ")

say_hi(name)