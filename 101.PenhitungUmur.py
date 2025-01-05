from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    birthdate = datetime.strptime(birthdate, "%d-%m-%Y")
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

birthdate = iput("Masukkan tagggal lahir (dd-mm-yyyy): ")
age = calculate_age(birthdate)
print(f"Umur Anda: {age} tahun")
