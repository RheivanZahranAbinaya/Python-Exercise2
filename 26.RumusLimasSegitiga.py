print('='*25)
print('PROGRAM LIMAS SEGITIGA')
print('='*25)

la = float(input("Masukkan Luas Alas: "))
ls = float(input('Masukan Luas Selubung: '))
t = float(input('Masukan Tinggi: '))
luas = la + ls
volume = 1/3 * la * t

print('Luas Permukaan\t: ' , round(luas,2), 'Cm2')
print('Volume\t\t: ' , round(volume,2), 'Cm3')