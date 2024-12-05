# Fungsi untuk memeriksa apakah sebuah kata adalah palindrome
def is_palindrome(word):
    # Menghilangkan spasi dan mengubah huruf menjadi kecil untuk perbandingan
    word = word.replace(" ", "").lower()
    
    # Membalikkan kata dan memeriksa apakah sama dengan kata asli
    return word == word[::-1]

# Fungsi untuk menghitung jumlah vokal dalam sebuah string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Fungsi utama
def main():
    print("Selamat datang di program Python!")
    
    # Loop untuk menjalankan program berulang kali
    while True:
        # Input dari pengguna untuk memeriksa palindrome
        word = input("Masukkan sebuah kata atau kalimat untuk memeriksa apakah itu palindrome (atau ketik 'exit' untuk keluar): ")
        
        # Mengecek apakah pengguna ingin keluar
        if word.lower() == 'exit':
            print("Terima kasih telah menggunakan program ini!")
            break
        
        # Cek apakah kata tersebut palindrome
        if is_palindrome(word):
            print(f"'{word}' adalah palindrome!")
        else:
            print(f"'{word}' bukan palindrome.")
        
        # Input dari pengguna untuk menghitung jumlah vokal
        text = input("Masukkan teks untuk menghitung jumlah vokalnya: ")

        # Hitung jumlah vokal
        vowel_count = count_vowels(text)
        if vowel_count > 0:
            print(f"Teks yang Anda masukkan mengandung {vowel_count} vokal.")
        else:
            print("Tidak ada vokal dalam teks yang Anda masukkan.")
        
        # Menanyakan apakah ingin mencoba lagi
        try_again = input("Apakah Anda ingin mencoba lagi? (y/n): ").lower()
        if try_again != 'y':
            print("Terima kasih telah menggunakan program ini!")
            break

# Menjalankan program utama
if __name__ == "__main__":
    main()
