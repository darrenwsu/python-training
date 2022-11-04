"""
Nhap vao mot so
kiem tra so do duong, am hay bang 0
"""
so = float(input('enter the number: '))
if so > 0:
    print(so, 'la so duong')
elif so < 0:
    print(so, 'la so am')
else:
    print('so 0')
