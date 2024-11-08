#TP4_3_H071241020
def hitung_langkah(n):
    """Menghitung jumlah langkah hingga n menjadi 1 berdasarkan aturan yang diberikan."""
    langkah = 0

    while n != 1:
        print(f"{n}")  # Menampilkan nilai n pada setiap langkah
        if n % 2 == 0:
            n = n // 2  # Jika n genap, bagi 2
        else:
            n = n * 3 + 1  # Jika n ganjil, kalikan 3 lalu tambahkan 1
        langkah += 1

    print(f"{n}")  # Tampilkan nilai 1 di akhir
    return langkah

def main():
    try:
        # Input dari pengguna
        n = int(input("Masukkan bilangan bulat positif : "))

        if n <= 0:
            raise ValueError  # Jika n bukan bilangan bulat positif, anggap sebagai input tidak valid

        # Hitung jumlah langkah hingga n menjadi 1
        jumlah_langkah = hitung_langkah(n)

        # Tampilkan hasil jumlah langkah
        print(f"Jumlah langkah : {jumlah_langkah}")


    except ValueError:
        print("Input tidak Valid")

# Jalankan program utama
main()
