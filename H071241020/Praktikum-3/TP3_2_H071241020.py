#TP3_2_H071241020
 #Seorang pemain sedang bermain permainan menebak angka. Komputer memilih
#angka acak antara 1 hingga 100. Pemain diminta menebak angka tersebut dengan
#maksimal 5 kali percobaan. Jika pemain berhasil menebak dengan benar, permainan
#berakhir. Jika angka yang ditebak lebih besar dari angka rahasia, komputer akan
#memberikan pesan "Angka terlalu besar". Jika lebih kecil, pesan "Angka terlalu kecil"
#muncul. Pemain dapat menghentikan permainan kapan saja dengan mengetik '0'.
#Hint:
#Gunakan randint() dari library random untuk menentukan angka acak 1-1003
import random

# Komputer memilih angka acak antara 1 hingga 100
angka_rahasia = random.randint(1, 100)

print("Selamat datang di permainan tebak angka!")
print("Komputer telah memilih angka antara 1 hingga 100.")
print("Anda memiliki 5 kali kesempatan untuk menebak angka.")
print("Ketik '0' jika ingin menghentikan permainan.")

# Pemain memiliki maksimal 5 kali percobaan
percobaan = 5

for i in range(percobaan):
    tebakan = int(input(f"Tebakan {i+1} : "))

    if tebakan == 0:
        print("Permainan dihentikan.")
        break

    elif tebakan == angka_rahasia:
        print(f"Selamat! Anda berhasil menebak angka dalam {i+1} percobaan.")
        break
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar.")
    else:
        print("Angka terlalu kecil.")

    if i == percobaan - 1:
        print(f"Maaf, Anda kehabisan percobaan. Angka rahasia adalah {angka_rahasia}.")
