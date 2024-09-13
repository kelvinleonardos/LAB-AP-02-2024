# Masukkan nilai dan persentase kehadiran
ni = int(input("Masukkan nilai mahasiswa : "))
khd = int(input("Masukkan persentase kehadiran mahasiswa : "))
nt = input("Apakah anda mengerjakan tugas tambahan dengan baik? (isi dengan ya atau tidak. Isi ya jika nilai anda di atas standar.) : ").lower()

# Kondisi
if 75 <= khd <= 100 and nt =="ya":
    if 85 <= ni <= 100:
        print("Anda lulus dengan predikat A.")
    elif 70 <= ni <= 84:
        print("Anda lulus dengan predikat B.")
    elif 60 <= ni <= 69:
        print("Anda lulus dengan predikat C.")
    elif ni < 60 and nt == "ya":
        print("Anda lulus dengan predikat C")
    elif ni < 60 and nt == "tidak":
        print("Anda tidak lulus, sampai jumpa di semester depan!")
else:
    khd < 75 
    print("Anda tidak lulus, sampai jumpa di semester depan!")