nilai = int(input("Masukkan nilai akhir: "))
kehadiran = int(input("Masukkan persentase kehadiran: "))

if kehadiran < 75:
    predikat = "Tidak Lulus"
else:
    match nilai:
        case n if n >= 80 and n <= 100:
            predikat = "A"
        case n if n >= 70 and n <= 84:
            predikat = "B"
        case n if n >= 60 and n <= 69:
            predikat = "C"
        case n if n < 60:
            tugas_tambahan = int(input("Masukkan nilai tugas tambahan: "))
            if tugas_tambahan >= 70:
                predikat = "C"
            else:
                predikat = "Tidak Lulus"

print(f"Predikat: {predikat}")