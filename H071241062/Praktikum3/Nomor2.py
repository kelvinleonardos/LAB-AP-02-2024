import random

angka = random.randint(1, 100)
kesempatan = 5

while True:
    try:
        angka_tebakan = int(input("Masukkan tebakan anda (0 untuk berhenti): "))
        
        if angka_tebakan == 0:
            print("Anda memilih untuk berhenti.")
            break
        elif angka_tebakan < angka:
            print("Angka terlalu kecil.")
            kesempatan -= 1
        elif angka_tebakan > angka:
            print("Angka terlalu besar.")
            kesempatan -= 1
        else:
            print("Selamat! Anda menebak angka dengan benar.")
            break

        if kesempatan == 0:
            print("Kesempatan habis. Anda kalah.")
            break
    except ValueError:
        print("Input tidak valid! Masukkan angka.")

