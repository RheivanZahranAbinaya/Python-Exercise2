import random

def cek_khodam(name):
    khodams = ["Kurma", "Big Dragon", "Naga", "Wak Haji", "Sigma Mewing", "Chinese Person"," The Most Normal Person"," CEBOL!!!!😱" ]
    khodams1 = ["Smart,Kind,evil"]
    chosen_khodam = random.choice(khodams)
    chosen_khodam1 = random.choice(khodams1)
    return f"Nama: {name}\nKhodam Anda: {chosen_khodam} {chosen_khodam1}"

nama_pengguna = input("Masukkan nama Anda: ")
hasil = cek_khodam(nama_pengguna)
print(hasil)