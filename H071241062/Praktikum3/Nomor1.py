while True:
    try:
        n = int(input("Masukkan Jumlah Tinggi (minimal 3): "))
        if n < 3:
            print("Masukkan angka yang lebih besar atau sama dengan 3.")
            continue
        break  
    except ValueError:
        print("Input tidak valid! Masukkan angka.")


for i in range (n + 1):
    if i == n:
        continue
    if i %2 == 0:
        continue
    else:
        bintang = "* " * i
        hasil = bintang.center(2*n," ")
        print(hasil)
    
for i in range (n,0,-1):
    if i %2 == 0:
        continue
    else:
        bintang = "* " * i
        hasil = bintang.center(2*n," ")
        print(hasil)