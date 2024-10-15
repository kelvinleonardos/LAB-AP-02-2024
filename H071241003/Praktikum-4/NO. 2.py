def treasure_hunt():
    jarak_total = 0
    bahaya = False
    
    while True:
        try:
            langkah = int(input("Masukkan jarak langkah yang ditempuh (meter) atau 0 untuk selesai: "))
            
            if langkah < 0:
                print("Input tidak valid. Langkah tidak bisa negatif.")
                continue
            elif langkah == 0:
                break
            elif langkah > 20:
                bahaya = True
                print("Langkah lebih dari 20 meter terdeteksi, ini berbahaya!")
            else:
                jarak_total += langkah
                print(f"Total jarak: {jarak_total} meter")

        except ValueError:
            print("Input tidak valid. Masukkan angka yang benar.")

    if bahaya:
        print("Tidak aman untuk menggali harta karun. Coba lagi!")
    elif jarak_total == 50:
        print("Aman! Kamu tepat menemukan harta karun dan menang!")
    else:
        print("Tidak menemukan harta karun. Coba lagi!")

treasure_hunt()
