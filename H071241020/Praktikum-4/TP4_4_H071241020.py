#TP4_4_H071241020
#kalkulator yang dibuat adalah kalkulator yang terpisah fungsi setiap operasinya
def penjumlahan(x, y):
    return x + y

def pengurangan(x, y):
    return x - y

def perkalian(x, y):
    return x * y

def pembagian(x, y):
    if y == 0:
        return "Pembagian dengan angka nol tidak diperbolehkan, ulangi dengan angka atau operasi yang lain!"
    else:
        return x / y

def operasi(n):
    if n == "+":
        return penjumlahan
    elif n == "-":
        return pengurangan
    elif n == "*":
        return perkalian
    elif n == "/":
        return pembagian
    else:
        return None  # Menangani operasi yang tidak valid

# Input dari pengguna
x = int(input("x = "))
y = int(input("y = "))
n = input("Masukkan operasi (+, -, *, /): ")

# Mendapatkan fungsi berdasarkan input operasi
operasi_terpilih = operasi(n)

# Memeriksa apakah operasi valid
if operasi_terpilih is not None:
    hasil = operasi_terpilih(x, y)
    print(f"Hasil: {hasil}")
else:
    print("Masukkan operasi yang valid (+, -, *, /)!")


# def kalkulator():
#     # Meminta input dua angka dari pengguna
#     try:
#         angka1 = float(input("Masukkan angka pertama: "))
#         angka2 = float(input("Masukkan angka kedua: "))

#         # Meminta pengguna untuk memilih operasi
#         print("Pilih operasi yang diinginkan:")
#         print("1. Penjumlahan (+)")
#         print("2. Pengurangan (-)")
#         print("3. Perkalian (*)")
#         print("4. Pembagian (/)")

#         operasi = input("Masukkan simbol operasi (+, -, *, /): ")

#         # Melakukan operasi berdasarkan input pengguna
#         if operasi == "+":
#             hasil = angka1 + angka2
#             print(f"Hasil: {angka1} + {angka2} = {hasil}")
#         elif operasi == "-":
#             hasil = angka1 - angka2
#             print(f"Hasil: {angka1} - {angka2} = {hasil}")
#         elif operasi == "*":
#             hasil = angka1 * angka2
#             print(f"Hasil: {angka1} * {angka2} = {hasil}")
#         elif operasi == "/":
#             if angka2 == 0:
#                 print("Error: Pembagian dengan nol tidak diperbolehkan!")
#             else:
#                 hasil = angka1 / angka2
#                 print(f"Hasil: {angka1} / {angka2} = {hasil}")
#         else:
#             print("Operasi tidak valid. Silakan masukkan salah satu dari (+, -, *, /).")

#     except ValueError:
#         print("Input tidak valid! Masukkan angka yang benar.")

# # Jalankan program kalkulator
# kalkulator()
