# Fungsi untuk menghasilkan semua substring dari string
def generate_substrings(string):
    length = len(string)
    substrings_by_length = {}

    # Loop untuk panjang substring mulai dari 1 hingga panjang string
    for i in range(length):
        for j in range(i + 1, length + 1):
            substring = string[i:j]
            substr_len = len(substring)
            
            # Memasukkan substring ke dalam dictionary berdasarkan panjangnya
            if substr_len not in substrings_by_length:
                substrings_by_length[substr_len] = []
            substrings_by_length[substr_len].append(substring)
    
    return substrings_by_length

# Fungsi utama untuk menerima input dan menampilkan hasil
def main():
    # Input string dari pengguna
    string = input("Masukkan sebuah string: ")
    
    # Menghasilkan semua substring, dikelompokkan berdasarkan panjang
    substrings_by_length = generate_substrings(string)
    
    # Menampilkan semua substring yang dihasilkan
    print("Semua substring yang mungkin adalah:")
    
    for length in sorted(substrings_by_length.keys()):
        for substring in substrings_by_length[length]:
            print(substring)
# Menjalankan program
if __name__ == "__main__":
    main()
