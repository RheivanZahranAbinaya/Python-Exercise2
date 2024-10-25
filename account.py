USERNAME = "CockiesUmarus@gmail.com"
PASSWORD = "12345678"

username = input("Masukan Username\t: ")
password = input("Masukan Password\t: ")

# Block Percabanan
if username != USERNAME:
    print('USERNAME tidak tersedia, SALAH! COBA INGAT INGAT DULU, KALO SALAH GANTI USERNAME NYA')
elif username == USERNAME and password != PASSWORD:
    print('Password salah, INGAT INGAT DULU YA HITAM!')
else:
    print("Selamat Datang ",username)