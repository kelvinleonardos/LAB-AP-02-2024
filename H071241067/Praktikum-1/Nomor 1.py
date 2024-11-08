hargaSahamHariIni = 105.0
hargaSahamKemarin  = float(input("Masukkan harga saham kemarin: "))
persentasePerubahan = ((hargaSahamHariIni - hargaSahamKemarin) / hargaSahamKemarin) * 100
                
rekomendasi = ["Jual", "Tahan", "Beli"]
index = (persentasePerubahan > 5) - (persentasePerubahan < -3 )

print(f"Perubahan persentase harga saham: {persentasePerubahan:.2f}%")

print(f"Rekomendasi investasi: {rekomendasi[index + 1]}")

