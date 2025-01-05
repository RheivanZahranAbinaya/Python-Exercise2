import random

choices = ["Gunting", "Batu", "Kertas"]
computer_choice = random.choice(choices)
user_choice = input("Pilih: Gunting, Batu, atau Kertas? ")

if user_choice == computer_choice:
    print(f"Seri! Komputer juga memilih {computer_choice}")
elif (user_choice == "Gunting" and computer_choice == "Kertas") or \
     (user_choice == "Batu" and computer_choice == "Gunting") or \
     (user_choice == "Kertas" and computer_choice == "Batu"):
    print(f"Anda menang! Komputer memilih {computer_choice}")

else:
    print(f"Anda kalah! Komputer memilih {computer_choice}")