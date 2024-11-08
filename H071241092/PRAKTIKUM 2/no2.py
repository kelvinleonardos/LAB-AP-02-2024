usia = int(input("masukkan usia : "))
anggota = input("apakah anda anggota?  (ya/tidak) : ").lower()

if usia >= 1 and usia < 5:
    harga_tiket = 0
elif usia >= 5 and usia <= 12:
    harga_tiket = 50000
elif usia >= 13 and usia <= 59:
    harga_tiket = 100000
else:
    harga_tiket = 70000

diskon = harga_tiket * 20 / 100 if anggota == "ya" else 0
harga = harga_tiket - diskon

print("harga tiket : Rp.", int(harga))


