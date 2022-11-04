"""
input: ba so thuc a, b, c

process:
- a = 0 => bx + c = 0
+ b != 0 => x = -c/b
+ b = 0 & c = 0 => vsn
+ b = 0 & c != 0 => vn
- a != 0
+ denta = b^2 - 4ac
+ denta > 0 => x1 = (-b + can(denta)) / (2a), x2 = (-b - can(denta)) / (2a)
+ denta = 0 => x1 = x2 = -b/2a
+ denta < 0 => vn

output: nghiem x
"""


a = float(input('enter the number a: '))
b = float(input('enter the number b: '))
c = float(input('enter the number c: '))

if a == 0:
    if b != 0:
        print(f'x = {-c/b}')
    elif c == 0:
        print('pt co vo so nghiem')
    else:
        print('pt vo nghiem')
else:
    denta = b ** 2 - 4 * a * c
    if denta > 0:
        x1 = (-b + denta ** 0.5)/(2*a)
        x2 = (-b - denta ** 0.5)/(2*a)
        print(f'x1 = {x1}, x2 = {x2}')
    elif denta == 0:
        x = (-b)/2*a
        print(f'x1 = x2 = {x}')
    else:
        print('pt vo nghiem')
