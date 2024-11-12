def kalkulator_sederhana():

  print("Selamat datang di Kalkulator Sederhana!")

  while True:
    try:
      angka1 = float(input("Angka pertama: "))
      angka2 = float(input("Angka kedua: "))
      operasi = input("Operasi (+,-, *, /): ")

      if operasi == '+':
        hasil = angka1 + angka2
      elif operasi == '-':
        hasil = angka1 - angka2
      elif operasi == '*':
        hasil = angka1 * angka2
      elif operasi == '/':
        if angka2 == 0:
          print("Pembagian dengan nol tidak diperbolehkan.")
        else:
          hasil = angka1 / angka2
      else:
        print("Operasi tidak valid. Gunakan +,-, *, atau /")
        continue

      print("Hasil:", hasil)
      break

    except ValueError:
      print("Input tidak valid: could not convert string to float")

if __name__ == "__main__":
  kalkulator_sederhana()