#TP4_2_H071241020
def langkah_aman(jarak):
    """Memeriksa apakah langkah lebih dari 20 meter, yang dianggap berbahaya."""
    if jarak > 20:
        return False
    return True

def temukan_harta_karun():
    total_distance = 0
    bahaya_terdeteksi = False

    print("Selamat datang di permainan mencari harta karun! Anda harus mencapai 50 meter untuk menemukan harta karun.")
    print("Ingat, langkah lebih dari 20 meter dianggap berbahaya!")

    while True:
        try:
            langkah = float(input("Masukkan jarak langkah yang ditempuh dalam meter (0 untuk berhenti): "))

            if langkah == 0:
                break
            elif langkah < 0:
                print("Langkah tidak bisa negatif! Masukkan nilai yang valid.")
                continue

            if not langkah_aman(langkah):
                bahaya_terdeteksi = True
                print("Langkah terlalu jauh! Tidak aman untuk menggali harta karun. Coba lagi!")
            else:
                total_distance += langkah
                print(f"Total jarak yang telah ditempuh: {total_distance} meter")

            if total_distance >= 50:
                break

        except ValueError:
            print("Input tidak valid! Masukkan angka untuk jarak langkah.")

    # Keputusan akhir setelah pemain berhenti
    if bahaya_terdeteksi:
        print("Tidak aman untuk menggali harta karun. Coba lagi!")
    elif total_distance == 50:
        print("Aman! Kamu tepat menemukan harta karun dan menang!")
    else:
        print("Tidak menemukan harta karun. Coba lagi!")

# Menjalankan permainan
temukan_harta_karun()
