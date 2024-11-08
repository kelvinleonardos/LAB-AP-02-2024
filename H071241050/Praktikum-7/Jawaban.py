daftar_film = {}
daftar_tiket =[]

# Fungsi manual untuk menghasilkan ID tiket unik
def generate_ticket_id():
    # Menghasilkan ID tiket berdasarkan input manual
    id_manual = input("Masukkan ID tiket (contoh format: TICK271020241530): ")
    return f"TICK{id_manual}" if not id_manual.startswith("TICK") else id_manual

# Fungsi untuk menyimpan tiket ke dalam file teks
def simpan_tiket(tiket):
    try:
        with open("tiket.txt", "a") as file:
            file.write(f"ID Tiket: {tiket['id']}\nFilm: {tiket['film']}\nWaktu: {tiket['waktu']}\n")
            file.write("="*30 + "\n")
    except Exception as e:
        print("Terjadi kesalahan saat menyimpan tiket:", e)

while True:
    print("--- Sistem Pemesanan Tiket Bioskop ---")
    print("1. Admin")
    print("2. Pengunjung")
    print("3. Keluar")
    peran = input("Pilih peran (1/2/3): ")

    if peran == "1":
        while True:
            print("--- Menu Admin ---")
            print("1. Tambah film")
            print("2. Hapus film")
            print("3. Tampilkan daftar film")
            print("4. Daftar tiket")
            print("5. Detail tiket")
            print("6. Hapus tiket")
            print("7. Kembali")
            menu_admin = input("Pilih opsi: (1/2/3/4/5/6/7): ")

            if menu_admin == "1":
                nama_film = input("Masukkan nama film yang ingin ditambahkan (atau tekan enter untuk kembali): ")
                if nama_film:
                    if nama_film in daftar_film:
                        print("Nama film sudah ada!")
                    else:
                        daftar_film[nama_film] = {"nama": nama_film}
                        print("Film berhasil ditambahkan.")
                else:
                    continue

            elif menu_admin == "2":
                nama_film = input("Masukkan nama film yang ingin dihapus: ")
                if nama_film in daftar_film:
                    del daftar_film[nama_film]
                    print("Film berhasil dihapus.")
                else:
                    print("Film tidak ditemukan.")

            elif menu_admin == "3":
                if daftar_film:
                    print("--- Daftar Film ---")
                    for film in daftar_film:
                        print(f"Film: {film}")
                else:
                    print("Tidak ada film tersedia.")

            elif menu_admin == "4":
                print("--- Daftar Tiket ---")
                if daftar_tiket:
                    for tiket in daftar_tiket:
                        print(f"ID Tiket: {tiket['id']} | Film: {tiket['film']}")
                else:
                    print("Belum ada tiket yang terjual.")

            elif menu_admin == "5":
                id_tiket = input("Masukkan ID tiket yang ingin dilihat: ")
                tiket = next((t for t in daftar_tiket if t["id"] == id_tiket), None)
                if tiket:
                    print(f"ID Tiket: {tiket['id']}\nFilm: {tiket['film']}\nWaktu: {tiket['waktu']}")
                else:
                    print("Tiket tidak ditemukan.")

            elif menu_admin == "6":
                id_tiket = input("Masukkan ID tiket yang ingin dihapus: ")
                tiket = next((t for t in daftar_tiket if t["id"] == id_tiket), None)
                if tiket:
                    daftar_tiket.remove(tiket)
                    print("Tiket berhasil dihapus.")
                else:
                    print("Tiket tidak ditemukan.")

            elif menu_admin == "7":
                break

    elif peran == "2":
        while True:
            print("--- Menu Pengunjung ---")
            print("1. Tampilkan daftar film")
            print("2. Beli tiket")
            print("3. Kembali")
            menu_pengunjung = input("Pilih opsi: (1/2/3): ")

            if menu_pengunjung == "1":
                if daftar_film:
                    print("--- Daftar Film ---")
                    for film in daftar_film:
                        print(f"Film: {film}")
                else:
                    print("Tidak ada film tersedia.")

            elif menu_pengunjung == "2":
                film_pilihan = input("Masukkan nama film yang ingin dibeli tiketnya: ")
                if film_pilihan in daftar_film:
                    tiket_id = generate_ticket_id()
                    
                    # Cek apakah ID tiket sudah ada di daftar_tiket
                    if any(t['id'] == tiket_id for t in daftar_tiket):
                        print("ID tiket sudah digunakan! Silakan masukkan ID yang berbeda.")
                    else:
                        waktu = input("Masukkan waktu tiket (format bebas): ")
                        tiket = {
                            "id": tiket_id,
                            "film": film_pilihan,
                            "waktu": waktu
                        }
                        daftar_tiket.append(tiket)
                        simpan_tiket(tiket)
                        print("Tiket berhasil dibeli!")
                else:
                    print("Film tidak ditemukan.")

            elif menu_pengunjung == "3":
                break

    elif peran == "3":
        print("Terima kasih telah menggunakan sistem kami.")
        break

    else:
        print("Input tidak valid, silakan coba lagi.")