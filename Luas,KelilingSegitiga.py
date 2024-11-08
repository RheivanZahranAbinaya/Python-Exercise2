# Fungsi untuk menghitung luas segitiga :D
def hitung_luas(alas, tinggi):
    return 0.5 * alas * tinggi

# Fungsi untuk menghitung keliling segitiga :P
def hitung_keliling(sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

# Input dari pengguna
alas = float(input("Masukkan panjang alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))
sisi1 = float(input("Masukkan panjang sisi pertama: "))
sisi2 = float(input("Masukkan panjang sisi kedua: "))
sisi3 = float(input("Masukkan panjang sisi ketiga: "))

# Inisialisasi variabel untuk loop
i = 0
max_iterasi = 1  # Hanya satu iterasi untuk menghitung luas dan keliling, INGAT YA :D

while i < max_iterasi:
    luas = hitung_luas(alas, tinggi)
    keliling = hitung_keliling(sisi1, sisi2, sisi3)
    print(f"Luas segitiga: {luas}")
    print(f"Keliling segitiga: {keliling}")
    i += 1