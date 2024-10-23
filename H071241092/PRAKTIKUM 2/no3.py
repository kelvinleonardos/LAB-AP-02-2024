nilai_akhir = float(input("masukkan nilai akhir : "))
presentase_kehadiran = int(input("masukkan presentase kehadiran : "))

if presentase_kehadiran >= 75:
    if (nilai_akhir >= 85) and (nilai_akhir <= 100):
        predikat = "lulus dengan predikat A"
    elif (nilai_akhir >= 70) and (nilai_akhir <= 84):
        predikat = "lulus dengan predikat B"
    elif (nilai_akhir >= 60) and (nilai_akhir <= 69):
        predikat = "lulus dengan predikat C"
    elif (nilai_akhir < 60):
        predikat = "tidak lulus"
else:
    predikat = "tidak lulus"

print(predikat)
