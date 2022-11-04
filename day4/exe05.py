"""
Nhap mot nam 2002
kiem tra xem nam do co phai la nam nhuan hay ko
"""

nam = int(input('enter the year: '))

if nam >= 0:
    if nam % 4 == 0 and nam % 100 != 0 or nam % 400 == 0:
        print(nam, 'la nam nhuan')
    else:
        print(nam, 'ko phai la nam nhuan')
else:
    print("Nam khong hop le")
