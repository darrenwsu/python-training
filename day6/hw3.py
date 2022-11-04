a = float(input('enter the number a: '))
b = float(input('enter the number b: '))
c = float(input('enter the number c: '))
d = float(input('enter the number d: '))


"""
input: 4 so thuc a, b, c, d
output: max(a, b, c, d)
logic:
max1 = max(a, b)
max2 = max(c, d)
max = max(max1, max2)
"""

# sln1 = a
# if a < b:
#     sln1 = b

# sln2 = c
# if c < d:
#     sln2 = d

# sln = sln1
# if sln1 < sln2:
#     sln = sln2

# print(f'so lon nhat la: {sln}')

print(f'so lon nhat la: {max(a, b, c, d)}')
