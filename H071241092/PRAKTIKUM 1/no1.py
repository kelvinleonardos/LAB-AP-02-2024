harga_saham_hari_ini = 105,0
harga_saham_kemarin = float(input("Masukkan harga saham kemarin : "))

perubahan_presentase = ((harga_saham_hari_ini - harga_saham_kemarin) / harga_saham_kemarin ) *100

beli = (perubahan_presentase > 5) *1
tahan = (perubahan_presentase <= 5) * (perubahan_presentase >= -3) *1
jual = (perubahan_presentase <- 3) *1

rekomendasi = beli*"beli" + tahan*"tahan" + jual*"jual"

print(f"perubahan harga:  {perubahan_presentase:.2f}%")
print(f"rekomendasi investasi : {rekomendasi}")