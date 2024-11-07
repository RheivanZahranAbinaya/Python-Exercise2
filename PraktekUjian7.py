# Ada inputan  3 angka tentukan angka terbesar dan terkecil

list = []
a1 = list.append(int(input('Masukan Angka Pertama: ')))
a2 = list.append(int(input('Masukan Angka Kedua: ')))
a3 = list.append(int(input('Masukan Angka Ketiga: ')))

ab = max(list)
ak = min(list)

print('Angka Terbesar: ',ab)
print('Angka Terkecil: ',ak)
