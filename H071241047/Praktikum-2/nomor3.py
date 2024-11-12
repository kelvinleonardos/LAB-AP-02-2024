nilai_akhir = float(input("Masukkan nilai akhir: "))
persentase_kehadiran = float(input("Masukkan persentase kehadiran: "))
nilai_rata_tugas_tambahan = float(input("Masukkan nilai rata-rata tugas tambahan: "))

if persentase_kehadiran < 75:
    print("Tidak Lulus (Kehadiran tidak memenuhi syarat)")
else:
    if nilai_akhir >= 85:
        print("Lulus dengan Predikat A")
    elif nilai_akhir >= 70:
        print("Lulus dengan Predikat B")
    elif nilai_akhir >= 60 or nilai_rata_tugas_tambahan >= 70:
        print("Lulus dengan Predikat C")
    else:
        print("Tidak Lulus")