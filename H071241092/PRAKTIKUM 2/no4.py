penggunaan_data = int(input("masukkan jumlah data yang digunakan (GB) : "))
waktu_penggunaan = input("apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)? ")
jenis_penggunaan = input ("apakah anda pengguna personal atau bisnis? ")

if penggunaan_data < 10 and waktu_penggunaan == 'off-peak' and jenis_penggunaan == 'personal' :
    paket = "paket A"
elif penggunaan_data >= 10 and penggunaan_data <= 50 and waktu_penggunaan == 'peak' and jenis_penggunaan == 'personal' :
    paket = "paket B"
elif penggunaan_data > 50 and waktu_penggunaan == 'peak' and (jenis_penggunaan == 'personal' or jenis_penggunaan == 'bisnis'):
    paket = "paket C"
elif penggunaan_data > 50 and waktu_penggunaan == 'off-peak' and jenis_penggunaan == 'bisnis' :
    paket = "paket D"
else :
    paket = "tidak ada paket yang cocok" 

print("paket yang sesuai : ", paket)
