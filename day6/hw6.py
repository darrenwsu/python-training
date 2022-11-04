tu_so_1 = int(input('nhap vao tu so 1: '))
mau_so_1 = int(input('nhap vao mau so 1: '))
tu_so_2 = int(input('nhap vao tu so 2: '))
mau_so_2 = int(input('nhap vao mau so 2: '))

"""
a/b + c/d = (ad + bc) / bd
"""
if mau_so_1 * mau_so_2 != 0:
    tong = (tu_so_1*mau_so_2 + mau_so_1*tu_so_2)/(mau_so_1*mau_so_2)
    hieu = (tu_so_1*mau_so_2 - mau_so_1*tu_so_2)/(mau_so_1*mau_so_2)
    tich = (tu_so_1*tu_so_2)/(mau_so_1*mau_so_2)
    thuong = (tu_so_1*mau_so_2)/(tu_so_2*mau_so_1)

    print(
        f'tong = {tong:.2f}\nhieu = {hieu:.2f}\ntich = {tich:.2f}\nthuong = {thuong:.2f}')

else:
    print('syntax error')
