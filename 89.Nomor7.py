# UJIAN, PERTANYAAN NOMOR 7
# NAME: RHEIVAN ZAHRAN ABINAYA
# CLASS: X RPL/PPLG 2
# NOMOR ABSEN: 35

def proses_angka(angka):
    if angka != 7 and angka != 8:
        angka += 20
    print(f"Hasil: {angka}")

angka = int(input("Masukkan angka: "))

proses_angka(angka)
