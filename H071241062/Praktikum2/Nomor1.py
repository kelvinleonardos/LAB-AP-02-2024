def Segitiga_Valid(a, b, c):
    return a + b > c and a + c > b and b + c > a


def Segitiga(a, b, c):
    if not Segitiga_Valid(a, b, c):
        return "Input tidak membentuk segitiga yang valid"
    elif a == b == c:
        return "Segitiga Sama Sisi"
    elif a == b or b == c or a == c:
        return "Segitiga Sama Kaki"
    else:
        return "Segitiga Sembarang"


a = float(input("Masukkan panjang sisi pertama: "))
b = float(input("Masukkan panjang sisi kedua: "))
c = float(input("Masukkan panjang sisi ketiga: "))


print(Segitiga(a, b, c))