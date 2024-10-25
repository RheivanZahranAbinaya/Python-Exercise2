print("="*40)
print("PROGRAM TABUNG")
print("="*40)

R = float(input("Masukan jari-jari :"))
T = float(input("Masukan Tinggi : "))

PHI = 3.14
V = PHI * R * R * T
LP = (2 * PHI * R * T) + (2 * (2 * PHI * R))

print("volume : ",V, "cm3")
print("luas permukaan : ",LP,"cm2")
