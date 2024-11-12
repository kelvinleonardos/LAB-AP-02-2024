def caesar_cipher(kata, pergeseran):
    hasil_kata = ""
    
    for i in kata:
        # Enkripsi huruf kecil
        if 'a' <= i <= 'z':
            kata_baru = chr((ord(i) - ord('a') + pergeseran) % 26 + ord('a')) # %26 untuk tidak lebih dari 26
            hasil_kata += kata_baru
        # Enkripsi huruf besar
        elif 'A' <= i <= 'Z':
            kata_baru = chr((ord(i) - ord('A') + pergeseran) % 26 + ord('A')) #beda biner huruf kecil dan huruf besar
            hasil_kata += kata_baru
        else:
            hasil_kata += i
            
    return hasil_kata

input_string = input("Masukkan string: ")
jumlah_pergeseran = int(input("Masukkan jumlah pergeseran: "))

hasil_string = caesar_cipher(input_string, jumlah_pergeseran)

print("Chiper :", hasil_string)
