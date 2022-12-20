# integer is a non-fractional number, like 1, 2, 45, -1, -2, and -100.

# Max size of a Python integer - no limit
num = 98762345098709872345000

print(num + 1)

string_100 = "100"
# string to int
int(string_100) # 100

# Float to Int
int(2.5) # 2

# int to string
str(200) # '200'

def int_check(name):
    if isinstance(name, int):
        print(name, 'is an Integer')
    else:
        print(name, 'is not an Integer')

int_check(200)
int_check('teste')
int_check(20.5)