sisi_a = float(input("Masukkan sisi a: "))
sisi_b = float(input("Masukkan sisi b: "))
sisi_c = float(input("Masukkan sisi c: "))

if sisi_a <= 0 or sisi_b <= 0 or sisi_c <= 0:
    print("Panjang sisi harus positif")
else:
    if sisi_a == sisi_b == sisi_c:
        print("Segitiga Sama Sisi")
    elif (sisi_a == sisi_b and sisi_a != sisi_c) or (sisi_a == sisi_c and sisi_a != sisi_b) or (sisi_b == sisi_c and sisi_b != sisi_a):
        print("Segitiga Sama Kaki")
    else:
        print("Segitiga Sembarang")