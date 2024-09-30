usia = int(input("Masukkan usia: "))


if usia < 5:  
    print("Gratis")  
    exit()
elif 5 <= usia <= 12:
     harga = 50000
elif 13 <= usia <= 59:
     harga = 100000
else:
    harga = 70000

anggota = input("Apakah Anda anggota? (ya/tidak): ").strip().lower() 
harga = harga * 0.80 if anggota == "ya" else harga
print(f"Harga tiket yang harus dibayar: Rp{harga}")