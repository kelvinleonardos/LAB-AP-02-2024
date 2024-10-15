def kalimat_to_singkatan(sentence):
    # Memecah kalimat menjadi daftar kata
    words = ''.join([word[0].upper() for word in sentence.split()])
    
    # Looping untuk mencetak huruf pertama setiap kata
    for word in words:
        print(word[0], end="")

# Contoh penggunaan
input_sentence = input("Masukkan sebuah kalimat : ")
kalimat_to_singkatan(input_sentence)
