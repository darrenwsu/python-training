"""
1. variables
2. data types
3. format strings
"""
# variable: a name for a value
x = 5

print(x)

x = 6
print(x)

# data types
"""
int: 5, 6, -1, 0
float: 4.5, 5.6, -1.24353857, 0.0
str: "hello", 'jack'
bool: True, False
"""
print(True, False)
print(type(x)) # int
print(type(1.0)) # float
print(type('a')) # str

print(type(1), type('a'))

# format strings
s1 = "Hello "
s2 = "world!"

print(s1 + s2) # Hello world!

print(f"{s1} - {s2}")

print(s1 + str(9))
print(f'{s1}{9}')
