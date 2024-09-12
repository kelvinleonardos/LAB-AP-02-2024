# Input dari User
Karakter = input("Masukkan karakter yang ingin dicari: ")
Kalimat = input("Masukkan Kata_atau_Kalimat: ")
# Menampilkan pesan

print(f'{Karakter} tidak di temukan dalam "{Kalimat}"'* (Karakter not in Kalimat )+ f'{Karakter} ditemukan dalam kalimat "{Kalimat}"'* (Karakter in Kalimat))