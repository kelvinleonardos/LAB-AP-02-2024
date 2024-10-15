#Masukkan status keanggotaan dan usia.
sk = input("Status keanggotaan (ya or tidak): ").lower()
thn = int(input("Berapa usia anda? : "))

#Harga tiket berdasarkan usia dan status keanggotaan.
if sk == "ya": 
    if thn >= 60:
        ht = 70000
    elif 13 <= thn <= 60:
        ht = 100000
    elif 5 <= thn <= 12:
        ht = 50000
    else:
        ht = 0
    ht = ht * 4/5
elif sk == "tidak":
    if thn >= 60:
        ht = 70000
    elif 13 <= thn <= 60:
        ht = 100000
    elif 5 <= thn <= 12:
        ht = 50000
    else:
        ht = 0

    print(f"Harga tiket anda adalah Rp.{ht:.3f}")
else: 
    print(f"Anda tidak memasukkan data dengan benar, mohon ulangi.")