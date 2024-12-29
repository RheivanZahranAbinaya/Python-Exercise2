# UJIAN, PERTANYAAN NOMOR 2
# NAME: RHEIVAN ZAHRAN ABINAYA
# CLASS: X RPL/PPLG 2
# NOMOR ABSEN: 35

from datetime import datetime

def tampilkan_tanggal():
    skrng = datetime.now()
    format_tanggal = skrng.strftime("%A, %d %B %Y, %H:%M")
    return format_tanggal

print(tampilkan_tanggal())

# skrng adalah sekarang