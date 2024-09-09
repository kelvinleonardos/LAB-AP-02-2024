# Input harga saham kemarin
harga_kemarin = float(input("Masukkan harga saham kemarin: "))
harga_hari_ini = float(105.0)  # Harga saham hari ini

# Hitung perubahan persentase
perubahan_persen = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100

# Tentukan rekomendasi berdasarkan perubahan persentase
rekomendasi = ["Jual", "Tahan", "Beli"][(perubahan_persen > -3) + (perubahan_persen > 5)]

# Tampilkan rekomendasi
print(f"Perubahan Persentase: {perubahan_persen:.2f}%")
print(f"Rekomendasi Investasi: {rekomendasi}")
