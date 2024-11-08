populasi_awal_a = int(input("Masukkan populasi awal serangga A: "))
populasi_awal_b = int(input("Masukkan populasi awal serangga B: "))
jumlah_hari = int(input("Masukkan jumlah hari: "))

for hari in range(1, jumlah_hari + 1):
    if hari % 2 == 1:  # Hari ganjil
        populasi_awal_a = int(populasi_awal_a * 1.3)  # Ganti ',' dengan '.'
        populasi_awal_b = int(populasi_awal_b * 1.5)  # Ganti ',' dengan '.'
    else:  # Hari genap
        populasi_awal_a = int(populasi_awal_a * 0.8)  # Ganti ',' dengan '.'
        populasi_awal_b = int(populasi_awal_b * 0.6)  # Ganti ',' dengan '.'

        if hari % 5 == 0:  # Setiap 5 hari
            populasi_awal_a = int(populasi_awal_a * 0.9)  # Ganti ',' dengan '.'
            populasi_awal_b = int(populasi_awal_b * 0.9)  # Ganti ',' dengan '.'
            print(f"Hari {hari}: predator memakan 10% populasi.")

    # Menampilkan populasi setiap hari
    print(f"Hari {hari} Serangga A: {populasi_awal_a}, Serangga B: {populasi_awal_b}")
