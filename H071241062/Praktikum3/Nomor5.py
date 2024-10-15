A = int(input("Masukkan populasi awal serangga A: "))
B = int(input("Masukkan populasi awal serangga B: "))
hari = int(input("Masukkan jumlah hari: "))

for i in range(1, hari + 1):
    if i % 5 == 0:
        print(f"hari {i}: predator memakan 10% populasi")
        A = A * 0.9 * 1.3  # Kurangi 10%, lalu tambahkan pertumbuhan 30%
        B = B * 0.9 * 1.5  # Kurangi 10%, lalu tambahkan pertumbuhan 50%
        print(f"hari {i}: Serangga A = {int(A)}, Serangga B = {int(B)}")
    elif i % 2 == 0:
        A = A * 0.8  # Mengurangi 20% populasi
        B = B * 0.6  # Mengurangi 40% populasi
        print(f"hari {i}: Serangga A = {int(A)}, Serangga B = {int(B)}")
    else:
        A = A * 1.3  # Tambahkan pertumbuhan 30%
        B = B * 1.5  # Tambahkan pertumbuhan 50%
        print(f"hari {i}: Serangga A = {int(A)}, Serangga B = {int(B)}")
