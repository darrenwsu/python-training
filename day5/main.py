"""
nhap vao mot so nguyen n
kiem tra va in xem n la
nguyen am chan, le
nguyen duong chan, le
"""
n = int(input('enter the number n: '))
if n == 0:  
    print('n la so khong')
else:
    s = 'nguyen'
    s += ' duong' if n > 0 else ' am'
    s += ' chan' if n % 2 == 0 else ' le'

    print(f"{n} la so {s}")