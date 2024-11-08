import random

angka_rahasia = random.randint(1, 100)
for i in range(5):
    tebakan = int(input("Masukkan tebakan Anda (0 untuk berhenti): "))
    if tebakan == angka_rahasia :
        print("Selamat! Anda menebak angka dengan benar.")
        break
    elif tebakan == 0 :
        print("permainan berhenti")
        break
    elif tebakan > angka_rahasia :
        print("Angka terlalu besar.")
    else :
        print("Angka terlalu kecil.")

if tebakan != angka_rahasia :
    print(f"anda kehabisan percobaan, angka rahasia adalah {angka_rahasia}")