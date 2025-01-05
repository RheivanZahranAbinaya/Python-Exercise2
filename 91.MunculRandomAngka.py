import random

def generate_random_numbers(n):
    return [random.randint(1, 100) for _ in range(n)]

n = int(input("Masukkan jumlah angka acak yang ingin dihasilkan: "))
print(f"Angka acak: {generate_random_numbers(n)}")