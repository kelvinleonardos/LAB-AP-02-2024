penggunaan_data = float(input("Masukkan rata-rata penggunaan data per bulan (GB): "))
jam_sibuk = input("Apakah mayoritas penggunaan di jam sibuk? (ya/tidak): ")
jenis_pengguna = input("Jenis pengguna (personal/bisnis): ")

if penggunaan_data < 10:
    kategori_data = "Ringan"
elif penggunaan_data <= 50:
    kategori_data = "Sedang"
else:
    kategori_data = "Berat"

if kategori_data == "Ringan" and jam_sibuk() == "tidak" and jenis_pengguna() == "personal":
    paket = "Paket A"
elif kategori_data == "Sedang" and jam_sibuk() == "ya" and jenis_pengguna() == "personal":
    paket = "Paket B"
elif kategori_data == "Berat" and jam_sibuk() == "ya":
    paket = "Paket C"
elif kategori_data == "Berat" and jam_sibuk() == "tidak" and jenis_pengguna() == "bisnis":
    paket = "Paket D"
else:
    paket = "Tidak ada paket yang cocok"

print("Rekomendasi paket:", paket)