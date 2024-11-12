harga = float(input("Masukkan total harga: "))
uang_dibayar = float(input("Masukkan jumlah uang yang dibayar: "))
kembalian = uang_dibayar - harga

pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

print("Kembalian:", kembalian)
print("Rincian:")
for p in pecahan:
    jumlah_pecahan = kembalian // p
    kembalian %= p
    if jumlah_pecahan > 0:
        print(f"{jumlah_pecahan} lembar {p}")