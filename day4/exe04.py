"""
ax^2 + bx + c = 0
if a = 0: 
    bx + c = 0
else:
    denta = b^2 - 4ac

    if denta > 0:
        x1 = (-b + denta ** 0.5) / (2a)
        x2 = (-b - denta ** 0.5) / (2a)
    elif denta == 0:
        x1 = x2 = -b / (2a)
    else:
        "vo nghiem"
"""
a = float(input('enter a: '))
b = float(input('enter b: '))
c = float(input('enter c: '))

if a == 0:
    if b != 0:
        print(-c/b)
    elif c == 0:
        print('pt co vo so nghiem')
    else:
        print('pt vo nghiem')
else:
    denta = b ** 2 - 4*a*c
    print(denta)
    if denta > 0:
        x1 = (-b + denta ** 0.5)/(2*a)
        x2 = (-b - denta ** 0.5)/(2*a)
        print(x1, x2)
    elif denta == 0:
        x = -b/(2*a)
        print(x)
    else:
        print('pt vo nghiem')
