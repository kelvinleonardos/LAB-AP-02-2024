import random

angka_rahasia = random.randint(1, 100)
percobaan = 0

while percobaan < 5:
    tebakan = int(input("Tebak angka (1-100) atau 0 untuk berhenti: "))
    if tebakan == 0:
        break
    percobaan += 1
    if tebakan == angka_rahasia:
        print("Selamat, Anda benar!")
        break
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar")
    else:
        print("Angka terlalu kecil")

if percobaan == 5 and tebakan != angka_rahasia:
    print("Anda kehabisan percobaan. Angka rahasianya adalah:", angka_rahasia)