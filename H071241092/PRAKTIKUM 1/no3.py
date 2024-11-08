jumlah_detik = int(input("masukkan jumlah detik :"))

jam = jumlah_detik // 3600
menit = (jumlah_detik % 3600) //60
detik = jumlah_detik % 60

format_waktu = f"{jam:02}:{menit:02}:{detik:02}"

print(format_waktu)