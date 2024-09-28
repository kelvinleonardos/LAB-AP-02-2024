import random

angka_rahasia = random.randint(1,100)

print("Selamat datang di permainan tebak angka!")
print("Saya telah memilih angka antara 1 hingga 100.")
print("Anda memiliki maksimal 5 kali percobaan untuk menebak angka.")
print("Ketik '0' untuk keluar dari permainan.")

for percobaan in range(5):
    print(f"\n Percobaan ke-{percobaan}")
    
    try:
        guess = int(input("Masukkan tebakan Anda (0 untuk berhenti) : "))
        if guess == 0:
            print("Anda telah keluar dari permainan.")
            break
        elif guess < 0:
            print("Angka tidak boleh dibawah 0")
        elif guess > 100:
            print("Angka tidak boleh diatas 100")
        elif guess == angka_rahasia:
            print(f"Selamat! Anda berhasil menebak angka yang benar adalah {angka_rahasia}.")
            break
        elif guess < angka_rahasia:
            print("Angka terlalu kecil.")
        else:
            print("Angka terlalu besar.")
        
        if percobaan == 5:
            print(f"Permainan selesai! Angka yang benar adalah {angka_rahasia}.")
    except:
        print("Harap memasukkan sebuah angka")