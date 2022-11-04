"""
input: hai so thuc a, b
process:
a != 0 => x = -b/a
a = 0 & b = 0 => vsn
a = 0 & b != 0 => vo nghiem
output: nghiem x
"""
a = float(input('enter the number a: '))
b = float(input('enter the number b: '))

if a != 0:
    print(f'x = {-b/a}')
elif b == 0:
    print('pt co vo so nghiem')
else:
    print('pt vo nghiem')
