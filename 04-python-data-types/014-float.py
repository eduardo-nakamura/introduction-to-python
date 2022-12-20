from math import floor, ceil

# float is a numerical data type that represents a floating-point number.
f = 1.45

# convert to float
float(2.0) # 2.0
float(2) # 2.0
float("2") # 2.0

f = 1.45e3 # 1450.0

x = 1.45
y = 4.51
# Add x and y
print(x + y) # 5.96
# Subtract x and y
print(x - y) # -3.0599999999999996
# Multiply x and y
print(x * y) # 6.539499999999999
# Divide x and y
print(x / y) # 0.3215077605321508

# Round, floor, and upper
f = 1.4567
print(round(f)) # 1
print(round(f, 2)) # 1.46

print(floor(1.23)) # 1
print(ceil(1.23)) # 2

if x == y:
    print("x and y are equal")
else:
    print("x and y are not equal")

# The Python float has limited precision
print(0.1 + 0.2) # 0.30000000000000004
print(round(0.1 + 0.2)) # 0

print(type(int(1.22))) # <class 'int'>
print(type(str(2.23))) # <class 'str'>