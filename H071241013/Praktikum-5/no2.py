def akronim(kalimat):
    kata_list = kalimat.split()
    akronim = ''.join([kata[0].upper() for kata in kata_list])
    return akronim

kalimat = input("Masukkan kalimat : ")
akronim = akronim(kalimat)
print(f"Akronim dari '{kalimat}' adalah: {akronim}")
