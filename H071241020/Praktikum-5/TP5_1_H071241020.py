#TP5_1_H071241020
def deteksi_palindrom(text):
    # Membersihkan teks dari spasi, kapitalisasi, dan karakter non-alphabet
    clean_text = ''.join(text.lower().split())
    
    # Memeriksa apakah teks sama jika dibaca dari depan dan belakang
    return clean_text == clean_text[::-1]

# Contoh penggunaan
input_teks = input("Masukkan kata atau kalimat : ")
if deteksi_palindrom(input_teks):
    print("Teks tersebut adalah palindrom.")
else:
    print("Teks tersebut bukan palindrom.")
