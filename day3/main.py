"""
Operators
+, -, *, /, //, %, **
>, <, >=, <=, ==, != return a boolean: True/False
and or not
"""
x = 5
y = 2.5

print(x, "+", y, "=",  x + y) # 7

print(x, '-', y, '=', x - y) # 3

print(x, '*', y, '=', x * y)

print(x, '/', y, '=', x / y)

print(x, '//', y, '=', x // y)

print(x, '%', y, '=', x % y)

print(x, '**', y, '=', x ** y)

print('-----------------------------------')

# print(1 / 0)
print(4 ** 0.5) # 2.0
print('a' + 'b') # ab
print(str(1) + 'c')

print('-----------------------------------')

print(1 > 3) # False
print(2.0 >= 2) # True
print(0.1 + 0.2) # 0.3000000000000004
print(0.1 + 0.2 == 0.3) # False

print(ord('a'), ord('b'))
print('ac' > 'b') # False

print("---------------------------------")

print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print("---------------------------------")

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print("---------------------------------")

print(not True) # False
print(not False) # True

print("---------------------------------")

"""
and tra ve gia tri dau tien khi no la False nguoc lai la gia tri thu hai
"""
print(bool(1)) # True
print(bool(0)) # False
print(1 and 2) # 2

print(bool('b'))
print(bool('')) # False
print('a' and 0) # 0

print('' and 0) # ''

print(bool(' ')) # True

print(1 > 2 and (3 < -6)) # False

print("---------------------------------")

"""
or tra ve gia tri dau tien khi no True nguoc lai gia tri thu hai
"""
print(1 or 2) # 1

print(bool(['']))
print([''] or '') # ['']

print(None or 1) # 1

print("------------------------------------------")

print(not None) # True
print(not 1) # False
