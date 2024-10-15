#TP2_4_H071241020
#Input data customer
pd = int(input("Berapa penggunaan anda dalam sebulan? (GB) : "))
wp = input("Mengakses internet lebih sering di luar jam sibuk (peak-off) atau di jam sibuk? : ")
jp = input("Penggunaan personal atau penggunaan bisnis? : ").lower()

#jenis paket 
if wp == "peak-off" : 
    if pd < 10 and jp == "penggunaan personal" : 
        print("Paket yang sesuai untuk anda adalah paket A.")
    elif pd > 50 and jp == "pengguna bisnis" :
        print("Paket yang sesuai  untuk anda adalah paket D.")
    else : 
        print("Tidak ada paket yang sesuai.")
elif wp == "peak" : 
    if 10 <= pd <= 50 and jp == "penggunaan personal":
        print("Paket yang sesuai untuk anda adalah paket B.")
    elif pd > 50 :
        print("Paket yang sesuai untuk anda adalah paket C.")
else :
    print("Tidak ada paket yang sesuai.")