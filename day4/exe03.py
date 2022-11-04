"""
Giai phuong trinh bac nhat mot an: ax + b = 0
input: Nhap hai so thuc a, b
output: nghiem x
process: neu a # 0 thi x = -b/a
nguoc lai b = 0 thi 0x + 0 = 0 => pt co vo so nghiem
nguoc lai => pt vo nghiem
"""
a = float(input('enter a: '))
b = float(input('enter b: '))

if a != 0:
    print(-b/a)
elif b == 0:
    print('pt co vo so nghiem')
else:
    print('pt vo nghiem')
