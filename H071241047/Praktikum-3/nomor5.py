populasi_A = int(input("Masukkan populasi awal serangga A: "))
populasi_B = int(input("Masukkan populasi awal serangga B: "))
hari = int(input("Masukkan jumlah hari: "))

for i in range(1, hari+1):
    if i % 2 == 1:
        populasi_A *= 1.3
        populasi_B *= 1.5
    else:
        populasi_A *= 0.8
        populasi_B *= 0.6
    if i % 5 == 0:
        populasi_A *= 0.9
        populasi_B *= 0.9

print(f"Setelah {hari} hari:")
print(f"Populasi serangga A: {populasi_A:.2f}")
print(f"Populasi serangga B: {populasi_B:.2f}")