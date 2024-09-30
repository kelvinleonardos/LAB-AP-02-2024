#TP3_5_H071241020
def prediksi_populasi(serangga_A, serangga_B, N):
    for hari in range(1, N + 1):
        print(f"\nHari {hari}:")

        # Pertumbuhan pada hari ganjil
        if hari % 2 == 1:
            serangga_A += serangga_A * 0.30  # Serangga A bertambah 30%
            serangga_B += serangga_B * 0.50  # Serangga B bertambah 50%
            print(f"Pertumbuhan hari ganjil: Serangga A = {serangga_A:.2f}, Serangga B = {serangga_B:.2f}")

        # Pengurangan pada hari genap
        else:
            serangga_A -= serangga_A * 0.20  # Serangga A berkurang 20%
            serangga_B -= serangga_B * 0.40  # Serangga B berkurang 40%
            print(f"Pengurangan hari genap: Serangga A = {serangga_A:.2f}, Serangga B = {serangga_B:.2f}")

        # Predator datang pada hari kelipatan 5
        if hari % 5 == 0:
            serangga_A -= serangga_A * 0.10  # Predator memakan 10% serangga A
            serangga_B -= serangga_B * 0.10  # Predator memakan 10% serangga B
            print(f"Predator datang: Serangga A = {serangga_A:.2f}, Serangga B = {serangga_B:.2f}")

    # Tampilkan populasi setelah N hari
    print(f"\nPopulasi setelah {N} hari: Serangga A = {serangga_A:.2f}, Serangga B = {serangga_B:.2f}")

# Input dari pengguna
serangga_A = float(input("Masukkan populasi awal Serangga A: "))
serangga_B = float(input("Masukkan populasi awal Serangga B: "))
N = int(input("Masukkan jumlah hari: "))

# Panggil fungsi prediksi
prediksi_populasi(serangga_A, serangga_B, N)
