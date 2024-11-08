

x = int(input("Masukkan jumlah detik: "))

jam = x//3600
menit = (x%3600)//60
detik = x%60

print(f"{jam:04d}:{menit:02d}:{detik:02d}")