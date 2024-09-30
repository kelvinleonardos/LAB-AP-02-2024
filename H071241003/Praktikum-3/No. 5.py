A = int(input("Masukkan populasi awal serangga A: "))
B = int(input("Masukkan populasi awal serangga B: "))
jumlah_hari = int(input("Masukkan jumlah hari: "))

if jumlah_hari > 0:
    for hari in range(1, jumlah_hari + 1):
        if hari > 0:
            if hari % 2 == 1:
                A = int(A * 1.3)
                B = int(B * 1.5)
            else:
                A = int(A * 0.8)
                B = int(B * 0.6)

            if hari % 5 == 0:
                A = B = int(A * 0.9)
                print(f'Hari ke {hari}: Predator memakan 10% populasi')

            if A <= 0 and B <= 0:
                print(f'Hari ke {hari}: Kedua serangga habis.')
                break

        A = max(0, A)
        B = max(0, B)

        print(f"Hari ke {hari}: Serangga A = {A} dan Serangga B = {B}")
else:
    print("Jumlah hari harus lebih dari 0")
