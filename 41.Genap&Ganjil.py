def cek_genap(angka):
    if angka % 2 == 0:
        return True
    else:
        return False

angka = int(input("Masukkan angka: "))

if cek_genap(angka):
    print(f"{angka} adalah angka genap.")
else:
    print(f"{angka} adalah angka ganjil.")

