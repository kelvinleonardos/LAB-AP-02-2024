def hitung_penghapusan(teks1, teks2):
    
    frekuensi_teks1 = {}
    for karakter in teks1:
        if karakter in frekuensi_teks1:
            frekuensi_teks1[karakter] += 1
        else:
            frekuensi_teks1[karakter] = 1

    jumlah_penghapusan = 0
    for karakter in frekuensi_teks1:
        if karakter in teks2:
            jumlah_penghapusan += max(0, frekuensi_teks1[karakter] - teks2.count(karakter))
        else:
            jumlah_penghapusan += frekuensi_teks1[karakter]

    return jumlah_penghapusan

teks1 = input("Masukkan string pertama: ")
teks2 = input("Masukkan string kedua: ")
print(f"Jumlah penghapusan minimum untuk membentuk anagram: {hitung_penghapusan(teks1, teks2)}")
