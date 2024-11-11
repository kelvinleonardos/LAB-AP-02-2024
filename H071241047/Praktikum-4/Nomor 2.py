def harta_karun():
    langkah_list = []
    bahaya = "no"  
    for i in range(5):
        langkah = input("Masukkan Langkah Anda:")
        try:
            langkah = int(langkah)
            if langkah <= 0:
                break
            elif langkah >= 20:
                bahaya = "ya"
            langkah_list.append(langkah)
        except ValueError:
            print("Masukkan ulang kode dalam bentuk angka")

    if langkah_list:
        total = sum(langkah_list)
        print("Total langkah:", total)
        if total == 50:
            if bahaya == "no":
                print("Keputusan: AMAN! Ayo Ambil Hartamu")
            else:
                print("Keputusan: Tidak Aman Untuk Digali, Coba Lagi")
        else:
            print("Tak ada Harta Karun Kawan, Coba Lagi")
    else:
        print("Tidak ada data langkah yang valid.")
    return langkah
print(harta_karun())