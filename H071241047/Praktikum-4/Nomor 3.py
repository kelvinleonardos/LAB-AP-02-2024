def hitung_langkah(n):
  langkah = 0
  while n != 1:
    if n <= 0:
      return -1  # Input tidak valid
    if n % 2 == 0:
      n = n // 2
    else:
      n = 3 * n + 1
    langkah += 1
    print(n)

  return langkah

# Input bilangan dari pengguna
n = int(input("Masukkan bilangan bulat positif: "))

# Panggil fungsi dan tampilkan hasil
hasil = hitung_langkah(n)
if hasil == -1:
  print("Input tidak Valid")
else:
  print("Jumlah langkah: ", hasil)