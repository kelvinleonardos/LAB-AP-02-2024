def buat_akronim(kalimat):
    kata_kata = kalimat.split() #Split membagi kalimat menjadi kata-kata UNHAS, KUAT , BERSATU
    akronim = ''.join(kata[0].upper() for kata in kata_kata)
    return akronim

kalimat = input("Masukkan kalimat: ")
print(buat_akronim(kalimat))