# Input nilai saham kemarin
nilai_kemarin = float(input("Masukkan nilai saham kemarin: "))
nilai_hari_ini = float(105.0)  # Nilai saham hari ini

# Hitung perubahan persentase
perubahan_persen = ((nilai_hari_ini - nilai_kemarin) / nilai_kemarin) * 100

# Tentukan rekomendasi berdasarkan perubahan persentase
rekomendasi = ["Jual", "Tahan", "Beli"][(perubahan_persen > -3) + (perubahan_persen > 5)]

# Tampilkan rekomendasi
print(f"Perubahan Persentase: {perubahan_persen:.2f}%")
print(f"Rekomendasi Investasi: {rekomendasi}")
