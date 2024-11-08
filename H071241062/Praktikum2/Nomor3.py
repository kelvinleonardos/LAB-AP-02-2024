nilai_akhir = float(input("Masukkan nilai akhir mahasiswa: "))
if nilai_akhir > 100:
    print("Nilai tidak valid")
    exit()
kehadiran = float(input("Masukkan persentase kehadiran mahasiswa: "))


if kehadiran < 75:
    predikat = "Tidak Lulus"
else:
    if nilai_akhir > 100:
        print("Lulus dengan Predikat A")
        exit()
    elif nilai_akhir >= 85:
        predikat = "Lulus dengan Predikat A"
    elif 70 <= nilai_akhir <= 84:
        predikat = "Lulus dengan Predikat B"
    elif 60 <= nilai_akhir <= 69:
        predikat = "Lulus dengan Predikat C"
    else:
        predikat = "Tidak Lulus"
      
    
print(f"Nilai Akhir: {nilai_akhir:.0f}")
print(f"Kehadiran: {kehadiran:.0f}%")
print(f"Predikat kelulusan mahasiswa: {predikat}")