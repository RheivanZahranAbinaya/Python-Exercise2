#Buatlah Program  untuk menentukan zat cair gas padat dengan  memasukan suhu zat tersebut

suhu = int(input('masukan suhu air: '))
if suhu > 100:
    print('udara')
elif suhu < 0:
    print('Padat')
else:
    print('cair')