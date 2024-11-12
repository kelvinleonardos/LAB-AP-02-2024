def acronym (a):
    akronim = ""
    for kata in a.split():
        akronim += kata[0]
    return akronim.upper()
a = str(input("Masukkan Kata: "))
print(acronym(a))