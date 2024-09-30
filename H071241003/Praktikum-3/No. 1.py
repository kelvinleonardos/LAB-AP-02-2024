try:
    n = int(input("Masukkan jumlah baris yang ingin ditampilkan (harus lebih dari 2) = "))
    if n < 3:
        print("Input tidak valid. Masukkan angka lebih dari 2.")
    else:
        m = n + 1
        for i in range(1, (m + 1) // 2):
            print('  ' * (n - i - 3) + '* ' * (2 * i - 1))
        
        for i in range((m // 2), 0, -1):
            print('  ' * (n - i - 3) + '* ' * (2 * i - 1))
except ValueError:
    print("Input tidak valid. Masukkan angka yang benar.")
