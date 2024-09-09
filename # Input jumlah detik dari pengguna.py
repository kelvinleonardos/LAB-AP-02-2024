# Input jumlah detik dari pengguna
jumlah_detik = int(input("Masukkan jumlah detik: "))

# Konversi ke jam, menit, dan detik
jam = jumlah_detik // 3600
menit = (jumlah_detik % 3600) // 60
detik = jumlah_detik % 60

# Format waktu dalam jam:menit:detik
waktu = f"{jam:02}:{menit:02}:{detik:02}"

# Tampilkan hasil
print(waktu)
