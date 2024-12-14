# UJIAN, PERTANYAAN NOMOR 8
# NAME: RHEIVAN ZAHRAN ABINAYA
# CLASS: X RPL/PPLG 2
# NOMOR ABSEN: 35

def kategori_angka(angka):
    if 100 <= angka < 1000:
        return "Ratusan"
    elif 1000 <= angka < 10000:
        return "Ribuan"
    elif 10000 <= angka < 1000000:
        return "Jutaan"
    else:
        return "angka tidak termasuk dalam kategori ratusan, ribuan, atau jutaan, LOL :D"

angka = int(input("Masukkan angka: "))

print(f"Angka {angka} termasuk dalam kategori: {kategori_angka(angka)}")
