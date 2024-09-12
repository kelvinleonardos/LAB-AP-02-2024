#input harga saham kemarin
harga_saham_kemarin = float(input('Masukkan harga saham kemarin: '))
harga_saham_hari_ini = 105

perubahan_persentase = (( harga_saham_hari_ini - harga_saham_kemarin)/ harga_saham_kemarin) *100

beli = perubahan_persentase >5
jual = perubahan_persentase <-3
tahan =  (perubahan_persentase <=5 ) and (perubahan_persentase >=-3)

rekomendasi = beli* 'BELI' + jual * 'jual'+ tahan * 'tahan'

#Menampilkan Pesan
print(f"Perubahan persentase harga saham: {perubahan_persentase:.2f}%")
print(f"Rekomendasi investasi: {rekomendasi}")