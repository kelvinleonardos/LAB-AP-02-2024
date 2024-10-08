# Fungsi Caesar Cipher untuk enkripsi
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""

    # Loop untuk setiap karakter di input
    for char in text:
        # Jika karakter adalah huruf kecil
        if char.islower():
            # Geser sesuai dengan jumlah pergeseran dan tetap dalam batas 'a' hingga 'z'
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        # Jika karakter adalah huruf besar
        elif char.isupper():
            # Geser sesuai dengan jumlah pergeseran dan tetap dalam batas 'A' hingga 'Z'
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        # Jika karakter bukan huruf (angka atau spesial), tetap seperti aslinya
        else:
            encrypted_text += char

    return encrypted_text

# Fungsi utama untuk input dan hasil enkripsi
def main():
    # Input string dari pengguna
    text = input("Masukkan string yang akan dienkripsi: ")

    # Input jumlah pergeseran (shift) dari pengguna
    while True:
        try:
            shift = int(input("Masukkan jumlah pergeseran (shift): "))
            if shift > 0:
                break
            else:
                print("Shift harus bilangan bulat positif.")
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat positif.")

    # Proses enkripsi menggunakan Caesar Cipher
    encrypted_text = caesar_cipher_encrypt(text, shift)

    # Menampilkan hasil enkripsi
    print("Hasil enkripsi:", encrypted_text)

# Menjalankan program
if __name__ == "__main__":
    main()
