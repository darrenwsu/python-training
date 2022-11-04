'''
input : luong dien tieu thu (kWh)
output : tien dien mot thang cong 10%gtgt
process: 
a(ldtt) <= 100 => a*550 
a(ldtt) <= 150 => 100 * 550 + (a - 100) * 
a(ldtt) <=200  => 100 * 550 + 50 * 900 + (a-150)*1250
a <= 300  =>  100 * 550 + 50 * 900 + 50* 1250 + (a - 200)*1450
else: 100 * 550 + 50 * 900 + 50* 1250 + 100 * 1450 + (a - 300 )*1700
a * 1.1

'''

a = int(input('luong dien tieu thu: '))

so_tien = 0
if a <= 100:
    so_tien = a * 550
elif a <= 150:
    so_tien = 100 * 550 + (a - 100) * 900
elif a <= 200:
    so_tien = 100 * 550 + 50 * 900 + (a-150)*1250
elif a <= 300:
    so_tien = 100 * 550 + 50 * 900 + 50 * 1250 + (a - 200)*1450
else:
    so_tien = 100 * 550 + 50 * 900 + 50 * 1250 + 100 * 1450 + (a - 300)*1700

so_tien *= 1.1
print(f'tien dien thang nay la: {int(so_tien)}')
