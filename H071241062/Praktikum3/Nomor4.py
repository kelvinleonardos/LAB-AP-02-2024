Harga = int(input("Masukkan total harga: "))
Uang = int(input("Masukkan uang yang diberikan: "))
mata_uang = [100000,50000,20000,10000,5000,2000,1000]
kembalian = Uang - Harga
for i in mata_uang:
    if Uang == Harga:
        print("uang pas")
        break
    elif Uang < Harga:
        print("Uang kurang")
        break
    else:
        a = kembalian // i 
        if a == 0:
            continue
        else :
            print(f"{a} lembar Rp {i:,}")
            kembalian = kembalian % i
