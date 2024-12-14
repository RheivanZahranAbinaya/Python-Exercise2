# UJIAN, PERTANYAAN NOMOR 5
# NAME: RHEIVAN ZAHRAN ABINAYA
# CLASS: X RPL/PPLG 2
# NOMOR ABSEN: 35

def tampilkan_buah():
    buah = input("masukkan 5 nama buah yang dipisahkan dengan koma: ")
    daftarbuah = buah.split(',')
    
    # menampilkan buah ke 2 dan ke4, 2 dan 4 ya! gak semua nya ya! :D
    if len(daftarbuah) >= 4:
        print(f"Buah ke-2: {daftarbuah[1]}")
        print(f"Buah ke-4: {daftarbuah[3]}")
    else:
        print("input tidak valid. Pastikan Anda memasukkan 5 nama buah.")

# MUAHAHAHAHAHA, Ini gabut doang ya :O
tampilkan_buah()
