print('='*10)
print('Kalkulator Sederhana2')
print('='*10)

d1 = float(input('Masukkan oprand 1: '))
o = input('Masukkan Operator: ')
o2 = float(input('Masukkan operand 2: '))

if o == '+':
    print('Hasilnya: ', d1 + o2)
elif o == '-':
    print('Hasilnya: ', d1 - o2)
elif o == '*':
    print('Hasilnya: ', d1 * o2)
elif o == '/':
    print('Hasilnya: ', d1 / o2)
elif o == '%':
    print('Hasilnya: ', d1 % o2)
else:
    print('Operator Salah')