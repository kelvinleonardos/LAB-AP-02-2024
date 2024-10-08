from collections import Counter

def min_deletions_to_make_anagram(str1, str2):
    # Hitung frekuensi karakter untuk kedua string
    count_str1 = Counter(str1)
    count_str2 = Counter(str2)

    # Inisialisasi jumlah penghapusan
    deletions = 0

    # Hitung karakter yang ada di str1 tetapi tidak ada di str2
    for char in count_str1:
        if char in count_str2:
            # Jika karakter ada di kedua string, hitung selisih frekuensinya
            deletions += abs(count_str1[char] - count_str2[char])
        else:
            # Jika karakter hanya ada di str1, hapus semuanya
            deletions += count_str1[char]

    # Hitung karakter yang ada di str2 tetapi tidak ada di str1
    for char in count_str2:
        if char not in count_str1:
            deletions += count_str2[char]

    return deletions

# Fungsi untuk menampilkan menu input dan hasilnya
def main():
    print("Selamat datang di Program Anagram Checker!")
    print("Masukkan dua string untuk dihitung berapa banyak karakter yang perlu dihapus agar menjadi anagram.")
    
    # Input string dari pengguna
    str1 = input("Masukkan string pertama: ")
    str2 = input("Masukkan string kedua: ")

    # Menghitung jumlah penghapusan
    result = min_deletions_to_make_anagram(str1, str2)
    
    # Menampilkan hasil
    print(f"Jumlah penghapusan minimum untuk membuat '{str1}' dan '{str2}' menjadi anagram sebanyak {result} karakter.")

# Menjalankan program
if __name__ == "__main__":
    main()
