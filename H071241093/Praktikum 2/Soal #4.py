#SOAL 4
x = int(input('Masukkan jumlah data yang digunakan(GB):')) #penggunaan data
y = input('Apakah mayoritas pengunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak) ?')#waktu pengunaan
z = input('Apakah anda pengguna personal atau bisnis ?') #jenis pengguna

if x < 10 and y == "off-peak" and z == "personal" :
  paket = "A"
elif  10<= x <= 50 and y=='peak' and z == 'personal':
  paket = "B"
elif x > 50 and y== "peak" and  z== ['personal','bisnis'] :
  paket = "C"
elif x > 50 and y== "off-peak" and z== "bisnis" :
  paket = "D"
else :
  paket = "data tidak valid"

print (f' paket yang sesuai : paket {paket}')




