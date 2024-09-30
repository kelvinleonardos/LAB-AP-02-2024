#TP3_1_H071241020
# Input jumlah baris (tinggi setengah belah ketupat)
n = int(input("Masukkan jumlah baris : "))

bilangan_ganjil = n % 2 != 0
lebar_max = (n if bilangan_ganjil else n - 1) * 2 - 1

for i in range(1, n // 2 + 1):
    print(("* " * (2 * i - 1)).center(lebar_max))
if bilangan_ganjil:
    print(("* " * n).center(lebar_max))
for i in range(n // 2, 0, -1):
    print(("* " * (2 * i - 1)).center(lebar_max))