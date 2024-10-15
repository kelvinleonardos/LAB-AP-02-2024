def tambah(angka1, angka2):
    return angka1 + angka2

def kurang(angka1, angka2):
    return angka1 - angka2

def kali(angka1, angka2):
    return angka1 * angka2

def bagi(angka1, angka2):
    if angka2 != 0:
        return angka1 / angka2
    else:
        return "Tidak bisa membagi dengan nol."

def kalkulator():
    try:
        print("Selamat datang di kalkulator sederhana!")

        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))

        operasi = input("Masukkan operasi yang diinginkan (+, -, *, /): ")
    
        if operasi == "+":
            print("Hasil:", tambah(angka1, angka2))
        elif operasi == "-":
            print("Hasil:", kurang(angka1, angka2))
        elif operasi == "*":
          print("Hasil:", kali(angka1, angka2))
        elif operasi == "/":
            print("Hasil:", bagi(angka1, angka2))
        else:
            print("Operasi tidak valid. Silakan coba lagi.")
    except ValueError:
        print("Input tidak valid")

kalkulator()