def enkripsi(teks, geser):

  abjad = "abcdefghijklmnopqrstuvwxyz"
  hasil = ""
  for karakter in teks:
    if karakter.lower() in abjad:
      index = abjad.find(karakter.lower())
      index_baru = (index + geser) % len(abjad)
      karakter_baru = abjad[index_baru]
      karakter_baru = karakter_baru.upper() if karakter.isupper() else karakter_baru
      hasil += karakter_baru
    else:
      hasil += karakter
  return hasil

teks = input("Masukkan String: ")
geser = int(input("Masukkan jumlah pergeseran: "))

cipher_teks = enkripsi(teks, geser)
print(f"teks: {teks}")
print(f"geser: {geser}")
print(f"cipher: {cipher_teks}")