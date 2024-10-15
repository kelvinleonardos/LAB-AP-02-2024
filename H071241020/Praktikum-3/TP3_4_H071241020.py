#TP3_4_H071241020
def hitung_kembalian(total_harga, uang_diberikan):
    # Daftar pecahan uang yang tersedia
    pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

    # Hitung kembalian
    kembalian = uang_diberikan - total_harga

    if kembalian < 0:
        return "Uang yang diberikan tidak cukup untuk membayar total harga."

    print(f"Kembalian: Rp {kembalian}")
    print("Rincian kembalian:")

    # Hitung jumlah lembaran per pecahan
    for pecahan in pecahan_uang:
        jumlah_lembar = kembalian // pecahan  # Hitung jumlah lembar per pecahan
        if jumlah_lembar > 0:
            print(f"{int(jumlah_lembar)} lembar Rp {pecahan}")
        kembalian %= pecahan  # Sisa kembalian setelah dikurangi pecahan

# Input dari pengguna
total_harga = int(input("Masukkan total harga yang harus dibayarkan: Rp "))
uang_diberikan = int(input("Masukkan jumlah uang yang diberikan: Rp "))

# Panggil fungsi hitung kembalian
hitung_kembalian(total_harga, uang_diberikan)