print('='*15)
print('PROGRAM BOLA')
print('='*15)

r = float(input("Masukkan Jari-Jari: "))
luas = 4 * 3.14 * r**2
keliling = 2 * 3.14 * r
volume = 4/3 * 3.14 * r**3

print('Keliling\t: ' , round(keliling,2), 'Cm')
print('Luas Permukaan\t: ' , round(luas,2), 'Cm2')
print('Volume\t\t: ' , round(volume,2), 'Cm3')