import time

def Waktu(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    print('Waktu habis!')

t = int(input("Masukkan waktu mundur dalam detik: "))
Waktu(t)