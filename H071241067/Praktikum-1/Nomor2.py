karakter = input("Masukkan Karakter: ")
kalimat = input("Masukkan Kalimat: ")

hasil = f"Karakter {karakter} merupakan bagian dari '{kalimat}'" * (karakter in kalimat) + \
        f"Karakter {karakter} tidak ditemukan dalam '{kalimat}'" * (karakter not in kalimat)
print(karakter in kalimat)
