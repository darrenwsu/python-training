a = float(input('enter the number a: '))
b = float(input('enter the number b: '))
c = float(input('enter the number c: '))

if a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and a + c > b:
    p = 0.5 * (a + b + c)
    S = (p * (p-a) * (p-b) * (p-c)) ** 0.5
    print(
        f'a,b,c tao thanh tam giac voi chu vi va dien tich lan luot la {2 * p:.2f}, {S:.2f}')
else:
    print('a,b,c khong tao thanh tam giac')
