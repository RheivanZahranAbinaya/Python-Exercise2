# perhitungan data di list
total = rata2 = max = min = 0
for data in nilai:
    total += data
    if data > max:
        max = data


    min = data
    if data < min:
        min = data


print(total)
print(f"Rata-rata : {total/jml}")
print(f"Nilai terbesar : {max}")
print(f"Nilai terkecil ; {min}")