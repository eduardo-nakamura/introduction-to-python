import sys
if  len(sys.argv) == 2: # breakpoint
    name = sys.argv[1]
else:
    name = 'stranger'
print(f'Hi there, {name}')