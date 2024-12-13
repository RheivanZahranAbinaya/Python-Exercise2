nilai_minimum = 75


kelulusan = lambda nilai: "Lulus" if nilai >= nilai_minimum else "Tidak Lulus"
nilai = int(input("Masukkan nilai: "))


hasil = kelulusan(nilai)
print(f"Nilai: {nilai}, Status: {hasil}")