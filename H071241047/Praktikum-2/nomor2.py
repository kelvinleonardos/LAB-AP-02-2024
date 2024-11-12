usia = int(input("Masukkan usia: "))
anggota = input("Apakah anggota (ya/tidak)? ")

if usia < 5:
    harga = 0
elif usia <= 12:
    harga = 50000
elif usia <= 59:
    harga = 100000
else:
    harga = 70000

if anggota.lower() == 'ya':
    harga *= 0.8

print("Harga tiket:", harga)