# UJIAN, PERTANYAAN NOMOR 3
# NAME: RHEIVAN ZAHRAN ABINAYA
# CLASS: X RPL/PPLG 2
# NOMOR ABSEN: 35

import math

def volume_tabung(radius, tinggi):
    volume = math.pi * (radius ** 2) * tinggi
    return volume

radius = float(input("masukkan jari-jari tabung (dalam satuan meter): "))
tinggi = float(input("masukkan tinggi tabung (daam satuan meter): "))

hasil_volume = volume_tabung(radius, tinggi)
print(f"volume tabung adalah: {hasil_volume} meter kubik")
