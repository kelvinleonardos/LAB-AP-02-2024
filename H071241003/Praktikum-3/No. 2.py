import random as rd

angka_rahasia = rd.randint(1, 100)

kesempatan = 5

while kesempatan > 0:
    try:
        tebakan = int(input("Masukkan tebakan Anda (0 untuk berhenti): "))
    except ValueError:
        print("Input harus berupa angka. Coba lagi.")
        kesempatan -= 1
        continue

    if tebakan == 0:
        print("Permainan dihentikan.")
        break

    if tebakan == angka_rahasia:
        print("Selamat! Tebakanmu benar.")
        break
    elif tebakan < angka_rahasia:
        print("Tebakanmu terlalu rendah.")
    else:
        print("Tebakanmu terlalu tinggi.")

    kesempatan -= 1

if kesempatan == 0:
    print(f"Kesempatan habis. Angka rahasia adalah {angka_rahasia}")
