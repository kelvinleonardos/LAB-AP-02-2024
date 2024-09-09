# Input dari pengguna
karakter = input("Masukkan karakter yang ingin dicari: ")
kalimat = input("Masukkan kalimat: ")

# Gunakan operator 'in' untuk memeriksa keberadaan karakter dalam kalimat
pesan = ("Karakter tidak ditemukan dalam Kalimat", "Karakter merupakan bagian dari Kalimat")[karakter in kalimat]

# Munculkan pesan
print(pesan)
