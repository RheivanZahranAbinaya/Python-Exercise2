print('='*20)
print('PROGRAM PERSEGI')
print('='*20)

def persegi():
    sisi = float(input('Masukan Sisi: '))
    luas = lambda s: s * s
    keliling = lambda s: 4 * s

    print('Luas\t\t: ' , luas(sisi) , 'Cm2')
    print('Keliling\t: ' , keliling(sisi) , 'Cm')

persegi()