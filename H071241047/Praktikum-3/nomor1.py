baris = int(input("Masukkan Jumlah Baris: "))

for i in range(baris):
    for j in range(baris - i - 1):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print()

for i in range(baris-2, -1, -1):
    for j in range(baris - i - 1):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print()