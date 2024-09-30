penggunaan_data = float(input("Masukkan penggunaan data (GB per bulan): "))
waktu_penggunaan = input("Masukkan waktu penggunaan (peak/off-peak): ").strip().lower()
jenis_pengguna = input("Masukkan jenis pengguna (personal/bisnis): ").strip().lower()


if penggunaan_data < 10 and waktu_penggunaan == "off-peak" and jenis_pengguna == "personal":
    paket = "Paket A"
elif 10 <= penggunaan_data <= 50 and waktu_penggunaan == "peak" and jenis_pengguna == "personal":
    paket = "Paket B"
elif penggunaan_data > 50 and waktu_penggunaan == "peak":
    paket = "Paket C"
elif penggunaan_data > 50 and waktu_penggunaan == "off-peak" and jenis_pengguna == "bisnis":
    paket = "Paket D"
else:
    paket = "Tidak ada paket yang cocok"


print(f"Paket layanan yang sesuai: {paket}")