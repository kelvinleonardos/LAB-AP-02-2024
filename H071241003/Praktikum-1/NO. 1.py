print("## Menghitung Harga Saham ##")
print("===========================")
print()

harga_kemarin = float(input("Masukkan harga saham kemarin: "))
harga_hari_ini = 105

perubahan_persentase = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100

rekomendasi = ["Jual", "Tahan", "Beli"]

index = (perubahan_persentase > 5) * 2 + (perubahan_persentase >= -3) * (perubahan_persentase <= 5)

print(f"Perubahan persentase: {perubahan_persentase:.2f}%")
print(f"Rekomendasi investasi: {rekomendasi[index]}")
