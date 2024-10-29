#TP7_H071241020
# Khaerurrozikin adalah seorang nazi programmer yang berfokus dalam bidang sistem
# informasi cerdas. Oleh karena itu, Erul (nama panggilannya) ditugaskan oleh client-nya sebut
# saja XXII untuk membuat aplikasi sistem informasi bioskop. Akan tetapi, Erul perlu bantuan
# kalian dalam mengerjakan tugas tersebut. Berikut adalah ketentuan yang diberikan client
# untuk aplikasinya.
# Manajemen Film (Admin):
# ● Tambah Film: Admin bisa menambahkan film ke dalam daftar. Admin bisa nambah
# film suka-suka dia,
# ● Hapus Film: Admin bisa menghapus film dari daftar. Admin otoriter dapat
# menghapus film yang sedang tayang di bioskop
# ● Tampilkan Daftar Film: Admin dapat melihat film yang ada. Biar admin bisa tau
# apa yang mau ditonton hari ini.
# Pembelian Tiket (Pengunjung):
# ● Tampilkan Daftar Film: Pengunjung bisa melihat film yang tersedia. Biar
# pengunjung juga tau, masa admin doang yang tau.
# ● Beli Tiket: Pengunjung bisa membeli tiket untuk film yang dipilih. Gak usah ada
# input harga langsung beli, langsung bayar juga
# ● Simpan Informasi Tiket: Simpan informasi tiket dalam file teks. Jangan lupa juga
# simpan hati dia biar gak diambil orang
# Manajemen Tiket (Admin):
# ● Tampilkan Daftar Tiket: Admin dapat melihat semua tiket yang telah dibeli. Biar
# banyak ini fiturnya admin
# ● Tampilkan Detail Tiket: Admin dapat melihat detail tiket yang dipilih. Terkadang
# bukan cuman detail tiket aja yang perlu dikasih liat.
# ● Hapus Tiket: Admin bisa menghapus tiket. Tapi admin gak bisa hapus ingatan kamu
# sama mantan kamu
# Berbagai Fungsi Lainnya (Plus)
# ● Menghasilkan ID Tiket: Hasilkan ID tiket unik berdasarkan waktu saat ini. “Tiket
# TICK27122024093000! (TICK 27 Desember 2024 jam 09:30:00)
# ● Menyimpan Informasi Tiket: Simpan informasi tiket dalam format yang rapi. Gak
# pas ketemu doi rapi, format tiket juga kalo bisa rapi yah.
# ● Menangani Kesalahan Input: Duh kok error gini? Buatlah program menangani
# kesalahan input seperti pro!
import os
import datetime

# Fungsi untuk menambahkan film oleh admin
def tambah_film():
    judul = input("Masukkan judul film: ")
    with open("film.txt", "a") as file_film:
        file_film.write(judul + "\n")
    print(f"Film '{judul}' berhasil ditambahkan.\n")

# Fungsi untuk menghapus film oleh admin
def hapus_film():
    if os.path.exists("film.txt"):
        with open("film.txt", "r") as file_film:
            film_list = file_film.readlines()

        if film_list:
            print("Daftar Film:")
            for i, film in enumerate(film_list, 1):
                print(f"{i}. {film.strip()}")

            pilihan = int(input("Masukkan nomor film yang ingin dihapus: "))
            if 1 <= pilihan <= len(film_list):
                film_dihapus = film_list.pop(pilihan - 1)
                with open("film.txt", "w") as file_film:
                    file_film.writelines(film_list)
                print(f"Film '{film_dihapus.strip()}' berhasil dihapus.\n")
            else:
                print("Pilihan tidak valid.\n")
        else:
            print("Belum ada film yang didaftarkan.\n")
    else:
        print("Belum ada film yang didaftarkan.\n")

# Fungsi untuk menampilkan daftar film untuk pelanggan dan admin
def tampilkan_film():
    if os.path.exists("film.txt"):
        with open("film.txt", "r") as file_film:
            film_list = file_film.readlines()
        if film_list:
            print("Daftar Film yang Tersedia:")
            for i, film in enumerate(film_list, 1):
                print(f"{i}. {film.strip()}")
        else:
            print("Belum ada film yang didaftarkan.")
    else:
        print("Belum ada film yang didaftarkan.")
    print()

# Fungsi untuk membeli tiket oleh pelanggan
def beli_tiket():
    tampilkan_film()
    nomor_film = int(input("Masukkan nomor film yang ingin dibeli: "))
    
    if os.path.exists("film.txt"):
        with open("film.txt", "r") as file_film:
            film_list = file_film.readlines()

        if 1 <= nomor_film <= len(film_list):
            judul_film = film_list[nomor_film - 1].strip()

            # Membuat ID tiket berdasarkan waktu saat ini
            waktu_sekarang = datetime.datetime.now().strftime("TICK%d%m%Y%H%M%S")

            # Simpan data tiket ke file tiket.txt
            with open("ticket.txt", "a") as file_tiket:
                file_tiket.write(f"{waktu_sekarang},{judul_film}\n")
            print(f"Tiket untuk film '{judul_film}' berhasil dibeli dengan ID Tiket {waktu_sekarang}.\n")
        else:
            print("Nomor film tidak valid.")
    else:
        print("Belum ada film yang didaftarkan.")

# Fungsi untuk menampilkan daftar tiket yang telah dibeli
def tampilkan_tiket():
    if os.path.exists("ticket.txt"):
        with open("ticket.txt", "r") as file_tiket:
            tiket_list = file_tiket.readlines()
        if tiket_list:
            print("Daftar Tiket yang Telah Dibeli:")
            for i, tiket in enumerate(tiket_list, 1):
                # Pastikan setiap baris hanya dipisahkan menjadi dua komponen
                tiket_split = tiket.strip().split(",")
                if len(tiket_split) == 2:  # Memastikan ada dua komponen
                    id_tiket, film = tiket_split
                    print(f"{i}. ID Tiket: {id_tiket}, Film: {film}")
                else:
                    print(f"Baris data tiket tidak valid: {tiket.strip()}")
        else:
            print("Belum ada tiket yang dibeli.")
    else:
        print("Belum ada tiket yang dibeli.")
    print()

# Fungsi untuk menampilkan detail tiket berdasarkan ID tiket
# def detail_tiket():
#     tampilkan_tiket()
#     nomor_tiket = int(input("Masukkan nomor tiket yang ingin dilihat detailnya: "))

#     if os.path.exists("ticket.txt"):
#         with open("ticket.txt", "r") as file_tiket:
#             tiket_list = file_tiket.readlines()
        
#         if 1 <= nomor_tiket <= len(tiket_list):
#             id_tiket, film = tiket_list[nomor_tiket - 1].strip().split(",")

#             # Menambahkan format tanggal pada detail tiket
#             tanggal_sekarang = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

#             print(f"""
# ----------------------------------------
#                 TIKET BIOSKOP
# ----------------------------------------
# ID Tiket  : {id_tiket}
# Film      : {film}
# Tanggal   : {tanggal_sekarang}
# ----------------------------------------
# Terima kasih telah membeli tiket Anda!
# ----------------------------------------
#             """)
#         else:
#             print("Nomor tiket tidak valid.")
#     else:
#         print("Belum ada tiket yang dibeli.")
# Fungsi untuk menampilkan daftar tiket yang telah dibeli dalam format terformat dan menambahkannya ke txt
def detail_tiket():
    if os.path.exists("ticket.txt"):
        with open("ticket.txt", "r") as file_tiket:
            tiket_list = file_tiket.readlines()
        
        if tiket_list:
            print("Daftar Tiket yang Telah Dibeli:")
            for i, tiket in enumerate(tiket_list, 1):
                id_tiket, film = tiket.strip().split(",")
                tanggal_pembelian = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                # Menampilkan tiket dengan format terformat di terminal
                print(f"""
----------------------------------------
                TIKET BIOSKOP
----------------------------------------
ID Tiket  : {id_tiket}
Film      : {film}
Tanggal Pembelian: {tanggal_pembelian}
----------------------------------------
Terima kasih telah membeli tiket Anda!
----------------------------------------
                """)

                # Simpan data tiket terformat ke file tiket_terformat.txt
                with open("tiket_terformat.txt", "a") as file_tiket_terformat:
                    file_tiket_terformat.write(f"----------------------------------------\n")
                    file_tiket_terformat.write(f"                TIKET BIOSKOP\n")
                    file_tiket_terformat.write(f"----------------------------------------\n")
                    file_tiket_terformat.write(f"ID Tiket  : {id_tiket}\n")
                    file_tiket_terformat.write(f"Film      : {film}\n")
                    file_tiket_terformat.write(f"Tanggal Pembelian: {tanggal_pembelian}\n")
                    file_tiket_terformat.write(f"----------------------------------------\n")
                    file_tiket_terformat.write(f"Terima kasih telah membeli tiket Anda!\n")
                    file_tiket_terformat.write(f"----------------------------------------\n\n")
        else:
            print("Belum ada tiket yang dibeli.")
    else:
        print("Belum ada tiket yang dibeli.")
    print()

# Fungsi untuk menghapus tiket berdasarkan nomor tiket
def hapus_tiket():
    tampilkan_tiket()
    nomor_tiket = int(input("Masukkan nomor tiket yang ingin dihapus: "))

    if os.path.exists("ticket.txt"):
        with open("ticket.txt", "r") as file_tiket:
            tiket_list = file_tiket.readlines()

        if 1 <= nomor_tiket <= len(tiket_list):
            tiket_dihapus = tiket_list.pop(nomor_tiket - 1)
            with open("ticket.txt", "w") as file_tiket:
                file_tiket.writelines(tiket_list)
            print(f"Tiket '{tiket_dihapus.strip()}' berhasil dihapus.\n")
        else:
            print("Nomor tiket tidak valid.\n")
    else:
        print("Belum ada tiket yang dibeli.\n")

# Fungsi untuk menampilkan menu admin
def menu_admin():
    while True:
        print("Menu Admin:")
        print("1. Tambah film")
        print("2. Hapus film")
        print("3. Daftar tiket")
        print("4. Kembali ke menu utama")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tambah_film()
        elif pilihan == '2':
            hapus_film()
        elif pilihan == '3':
            menu_daftar_tiket()
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid!\n")

# Fungsi untuk menampilkan menu daftar tiket
def menu_daftar_tiket():
    while True:
        print("Menu Daftar Tiket:")
        print("1. Lihat daftar tiket")
        print("2. Lihat detail tiket")
        print("3. Hapus tiket")
        print("4. Kembali ke menu admin")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tampilkan_tiket()
        elif pilihan == '2':
            detail_tiket()
        elif pilihan == '3':
            hapus_tiket()
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid!\n")

# Fungsi untuk menampilkan menu pelanggan
def menu_pelanggan():
    while True:
        print("Menu Pelanggan:")
        print("1. Lihat daftar film")
        print("2. Beli tiket")
        print("3. Kembali ke menu utama")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tampilkan_film()
        elif pilihan == '2':
            beli_tiket()
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid!\n")

# Fungsi utama untuk menampilkan menu utama
def menu_utama():
    while True:
        print("Menu Utama:")
        print("1. Admin")
        print("2. Pelanggan")
        print("3. Keluar")
        pilihan = input("Pilih peran: ")
        if pilihan == '1':
            menu_admin()
        elif pilihan == '2':
            menu_pelanggan()
        elif pilihan == '3':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Masukkan dengan benar input yang dibutuhkan\n")

# Menjalankan program
if __name__ == "__main__":
    menu_utama()




# import os
# import datetime

# Fungsi untuk menambahkan film oleh admin
# def tambah_film():
#     judul = input("Masukkan judul film: ")
#     with open("film.txt", "a") as file_film:
#         file_film.write(judul + "\n")
#     print(f"Film '{judul}' berhasil ditambahkan.\n")

# # Fungsi untuk menghapus film oleh admin
# def hapus_film():
#     if os.path.exists("film.txt"):
#         with open("film.txt", "r") as file_film:
#             film_list = file_film.readlines()

#         if film_list:
#             print("Daftar Film:")
#             for i, film in enumerate(film_list, 1):
#                 print(f"{i}. {film.strip()}")

#             pilihan = int(input("Masukkan nomor film yang ingin dihapus: "))
#             if 1 <= pilihan <= len(film_list):
#                 film_dihapus = film_list.pop(pilihan - 1)
#                 with open("film.txt", "w") as file_film:
#                     file_film.writelines(film_list)
#                 print(f"Film '{film_dihapus.strip()}' berhasil dihapus.\n")
#             else:
#                 print("Pilihan tidak valid.\n")
#         else:
#             print("Belum ada film yang didaftarkan.\n")
#     else:
#         print("Belum ada film yang didaftarkan.\n")

# # Fungsi untuk menampilkan daftar film untuk pelanggan dan admin
# def tampilkan_film():
#     if os.path.exists("film.txt"):
#         with open("film.txt", "r") as file_film:
#             film_list = file_film.readlines()
#         if film_list:
#             print("Daftar Film yang Tersedia:")
#             for i, film in enumerate(film_list, 1):
#                 print(f"{i}. {film.strip()}")
#         else:
#             print("Belum ada film yang didaftarkan.")
#     else:
#         print("Belum ada film yang didaftarkan.")
#     print()

# # Fungsi untuk membeli tiket oleh pelanggan
# def beli_tiket():
#     tampilkan_film()
#     nomor_film = int(input("Masukkan nomor film yang ingin dibeli: "))
    
#     if os.path.exists("film.txt"):
#         with open("film.txt", "r") as file_film:
#             film_list = file_film.readlines()

#         if 1 <= nomor_film <= len(film_list):
#             judul_film = film_list[nomor_film - 1].strip()

#             # Membuat ID tiket berdasarkan waktu saat ini
#             waktu_sekarang = datetime.datetime.now().strftime("TICK%d%m%Y%H%M%S")

#             # Mendapatkan tanggal dan waktu pembelian tiket
#             tanggal_pembelian = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

#             # Format tiket yang akan disimpan
#             tiket_terformat = f"""
# ----------------------------------------
#                 TIKET BIOSKOP
# ----------------------------------------
# ID Tiket  : {waktu_sekarang}
# Film      : {judul_film}
# Tanggal Pembelian: {tanggal_pembelian}
# ----------------------------------------
# Terima kasih telah membeli tiket Anda!
# ----------------------------------------
#             """
            
#             # Simpan data tiket terformat ke file tiket_terformat.txt
#             with open("tiket_terformat.txt", "a") as file_tiket:
#                 file_tiket.write(tiket_terformat + "\n")
            
#             # Simpan juga tiket ke file tiket.txt (untuk pencatatan umum)
#             with open("ticket.txt", "a") as file_tiket_general:
#                 file_tiket_general.write(f"{waktu_sekarang},{judul_film},{tanggal_pembelian}\n")
            
#             print(f"Tiket untuk film '{judul_film}' berhasil dibeli dengan ID Tiket {waktu_sekarang}.\n")
#         else:
#             print("Nomor film tidak valid.")
#     else:
#         print("Belum ada film yang didaftarkan.")

# # Fungsi untuk menampilkan daftar tiket yang telah dibeli
# def tampilkan_tiket():
#     if os.path.exists("ticket.txt"):
#         with open("ticket.txt", "r") as file_tiket:
#             tiket_list = file_tiket.readlines()
#         if tiket_list:
#             print("Daftar Tiket yang Telah Dibeli:")
#             for i, tiket in enumerate(tiket_list, 1):
#                 # Pastikan setiap baris hanya dipisahkan menjadi dua komponen
#                 tiket_split = tiket.strip().split(",")
#                 if len(tiket_split) == 3:  # Memastikan ada tiga komponen
#                     id_tiket, film, tanggal_pembelian = tiket_split
#                     print(f"{i}. ID Tiket: {id_tiket}, Film: {film}, Tanggal Pembelian: {tanggal_pembelian}")
#                 else:
#                     print(f"Baris data tiket tidak valid: {tiket.strip()}")
#         else:
#             print("Belum ada tiket yang dibeli.")
#     else:
#         print("Belum ada tiket yang dibeli.")
#     print()

# # Fungsi untuk menampilkan detail tiket berdasarkan ID tiket
# def detail_tiket():
#     tampilkan_tiket()
#     nomor_tiket = int(input("Masukkan nomor tiket yang ingin dilihat detailnya: "))
#     if os.path.exists("ticket.txt"):
#         with open("ticket.txt", "r") as file_tiket:
#             tiket_list = file_tiket.readlines()
        
#         if 1 <= nomor_tiket <= len(tiket_list):
#             id_tiket, film, tanggal_pembelian = tiket_list[nomor_tiket - 1].strip().split(",")

#             # Menampilkan detail tiket
#             print(f"""
# ----------------------------------------
#                 TIKET BIOSKOP
# ----------------------------------------
# ID Tiket  : {id_tiket}
# Film      : {film}
# Tanggal Pembelian: {tanggal_pembelian}
# ----------------------------------------
# Terima kasih telah membeli tiket Anda!
# ----------------------------------------
#             """)
#         else:
#             print("Nomor tiket tidak valid.")
#     else:
#         print("Belum ada tiket yang dibeli.")

# # Fungsi untuk menghapus tiket berdasarkan nomor tiket
# def hapus_tiket():
#     tampilkan_tiket()
#     nomor_tiket = int(input("Masukkan nomor tiket yang ingin dihapus: "))

#     if os.path.exists("ticket.txt"):
#         with open("ticket.txt", "r") as file_tiket:
#             tiket_list = file_tiket.readlines()

#         if 1 <= nomor_tiket <= len(tiket_list):
#             tiket_dihapus = tiket_list.pop(nomor_tiket - 1)
#             with open("ticket.txt", "w") as file_tiket:
#                 file_tiket.writelines(tiket_list)
#             print(f"Tiket '{tiket_dihapus.strip()}' berhasil dihapus.\n")
#         else:
#             print("Nomor tiket tidak valid.\n")
#     else:
#         print("Belum ada tiket yang dibeli.\n")

# # Fungsi untuk menampilkan tiket yang terformat dari file tiket_terformat.txt
# def tampilkan_tiket_terformat():
#     if os.path.exists("tiket_terformat.txt"):
#         with open("tiket_terformat.txt", "r") as file_tiket:
#             tiket_list = file_tiket.read()
#         if tiket_list:
#             print("Daftar Tiket yang Telah Dibeli:\n")
#             print(tiket_list)
#         else:
#             print("Belum ada tiket yang dibeli.")
#     else:
#         print("Belum ada tiket yang dibeli.")
#     print()

# # Fungsi untuk menampilkan menu admin
# def menu_admin():
#     while True:
#         print("Menu Admin:")
#         print("1. Tambah film")
#         print("2. Hapus film")
#         print("3. Daftar tiket")
#         print("4. Kembali ke menu utama")
#         pilihan = input("Pilih menu: ")

#         if pilihan == '1':
#             tambah_film()
#         elif pilihan == '2':
#             hapus_film()
#         elif pilihan == '3':
#             menu_daftar_tiket()
#         elif pilihan == '4':
#             break
#         else:
#             print("Pilihan tidak valid!\n")

# # Fungsi untuk menampilkan menu daftar tiket
# def menu_daftar_tiket():
#     while True:
#         print("Menu Daftar Tiket:")
#         print("1. Lihat daftar tiket")
#         print("2. Lihat detail tiket")
#         print("3. Hapus tiket")
#         print("4. Kembali ke menu admin")
#         pilihan = input("Pilih menu: ")

#         if pilihan == '1':
#             tampilkan_tiket()
#         elif pilihan == '2':
#             detail_tiket()
#         elif pilihan == '3':
#             hapus_tiket()
#         elif pilihan == '4':
#             break
#         else:
#             print("Pilihan tidak valid!\n")

# # Fungsi untuk menampilkan menu pelanggan
# def menu_pelanggan():
#     while True:
#         print("Menu Pelanggan:")
#         print("1. Lihat daftar film")
#         print("2. Beli tiket")
#         print("4. Tampilkan format tiket")
#         print("3. Kembali ke menu utama")
#         pilihan = input("Pilih menu: ")

#         if pilihan == '1':
#             tampilkan_film()
#         elif pilihan == '2':
#             beli_tiket()
#         elif pilihan == '3':
#             tampilkan_tiket_terformat()
#         elif pilihan == '4' :
#            break
