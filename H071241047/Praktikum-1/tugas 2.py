karakter = input("Masukkan karakter: ")
kalimat = input("Masukkan kalimat: ")

kalimat_set = set(kalimat)

ada_dalam_kalimat = karakter in kalimat_set

pesan = f"Karakter {karakter} ada dalam {kalimat}"

print(pesan)