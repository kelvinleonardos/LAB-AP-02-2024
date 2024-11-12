kemarin = float(input("Masukkan harga saham kemarin: "))

perubahan = ((105 - kemarin) / kemarin) * 100

rekomendasi_list = ["Jual", "Tahan", "Beli"]

indeks_rekomendasi = int(perubahan > 5) + int(-3 <= perubahan <= 5)

rekomendasi = rekomendasi_list[indeks_rekomendasi]

print("Perubahan persentase harga:", perubahan, "%")
print("Rekomendasi investasi:", rekomendasi)