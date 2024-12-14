def segitiga():
    alas = float(input('Masukan Alas: '))
    tinggi = float(input('Masukan Tinggi: '))
    sisimiring = float(input('Masukan Sisi Miring: '))
    luas = lambda l: 1/2 * alas * tinggi
    a = alas
    b = tinggi
    c = sisimiring
    keliling = lambda k: a + b + c

    print('Luas\t\t: ' , luas(alas) , 'Cm2')
    print('Keliling\t: ' , keliling(alas) , 'Cm')

segitiga()