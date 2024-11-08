import os
from datetime import datetime

file_name = "daftar_film.txt"
folder_tiket = "folder_tiket.txt"
os.makedirs(folder_tiket, exist_ok=True)

def tampilkan_menu(menu_items):
    """Mencetak pilihan menu."""
    for item in menu_items:
        print(item)

def input_angka(prompt, batas_bawah=None, batas_atas=None):
    """Mendapatkan input angka dengan validasi."""
    try:
        angka = int(input(prompt))
        if (batas_bawah is not None and angka < batas_bawah) or (batas_atas is not None and angka > batas_atas):
            print(f"Input tidak valid. Masukkan angka antara {batas_bawah} dan {batas_atas}.")
            return None
        return angka
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return None

def menu_utama():
    while True:
        print(3 * "-", "Sistem Pemesanan Tiket Bioskop", 3 * "-")
        tampilkan_menu(["1. Admin", "2. Pengunjung", "3. Keluar"])
        peran = input("Pilih peran (1/2/3): ")
        if peran == "1":
            menu_admin()
        elif peran == "2":
            menu_pengunjung()
        elif peran == "3":
            print("Terima kasih telah menggunakan sistem pemesanan tiket bioskop!")
            break
        else:
            print("Opsi tidak valid, silakan pilih kembali.")

def menu_admin():
    while True:
        print(3 * "-", "Menu Admin", 3 * "-")
        tampilkan_menu(["1. Tambah film", "2. Hapus film", "3. Daftar Tiket", "4. Kembali"])
        opsi = input("Pilih opsi (1/2/3/4): ")
        if opsi == "1":
            tambah_film()
        elif opsi == "2":
            hapus_film()
        elif opsi == "3":
            daftar_tiket()
        elif opsi == "4":
            break
        else:
            print("Input tidak valid.")

def tambah_film():
    print(3 * "-", "Tambah Film", 3 * "-")
    film = input("Masukkan nama film yang ingin ditambahkan (atau tekan enter untuk kembali): ")
    if film:
        with open(file_name, "a") as file:
            file.write(film + "\n")
        print(f"Film '{film}' ditambahkan ke file {file_name}.")
    else:
        print("Input film kosong, kembali ke menu.")

def hapus_film():
    print(3 * "-", "Hapus Film", 3 * "-")
    print("Daftar Film:")
    try:
        with open(file_name, "r") as file:
            nama_film = file.readlines()
    except FileNotFoundError:
        print("File daftar film tidak ditemukan.")
        return

    for index, line in enumerate(nama_film, start=1):
        print(f"{index}. {line.strip()}")

    nomor_baris = input_angka("Masukkan nomor film yang ingin dihapus (atau 0 untuk kembali): ", 0, len(nama_film))
    if nomor_baris is None or nomor_baris == 0:
        return
    nama_film.pop(nomor_baris - 1)

    with open(file_name, "w") as file:
        file.writelines(nama_film)
    print("Film telah dihapus dari daftar.")

def daftar_tiket():
    while True:
        print(3 * "-", "Daftar Tiket", 3 * "-")
        tampilkan_menu(["1. Lihat Daftar Tiket", "2. Lihat Detail Tiket", "3. Hapus Tiket", "4. Kembali"])
        opsi = input("Pilih opsi (1/2/3/4): ")
        if opsi == "1":
            lihat_daftar_tiket()
        elif opsi == "2":
            lihat_detail_tiket()
        elif opsi == "3":
            hapus_tiket()
        elif opsi == "4":
            break
        else:
            print("Input tidak valid.")

def lihat_daftar_tiket():
    print("Daftar tiket:")
    tiket_files = os.listdir(folder_tiket)
    if not tiket_files:
        print("Tidak ada tiket yang tersedia.")
    else:
        for index, id_tiket in enumerate(tiket_files, start=1):
            print(f"{index}. {id_tiket}")

def lihat_detail_tiket():
    tiket_files = os.listdir(folder_tiket)
    if not tiket_files:
        print("Tidak ada tiket yang tersedia.")
        return

    nomor_tiket = input_angka("Masukkan nomor tiket yang ingin dilihat detailnya: ", 1, len(tiket_files))
    if nomor_tiket is None:
        return

    tiket_file_path = os.path.join(folder_tiket, tiket_files[nomor_tiket - 1])
    with open(tiket_file_path, "r") as file:
        detail_tiket = file.read()
    print(f"Detail Tiket:\n{detail_tiket}")

def hapus_tiket():
    tiket_files = os.listdir(folder_tiket)
    if not tiket_files:
        print("Tidak ada tiket yang tersedia.")
        return

    nomor_tiket = input_angka("Masukkan nomor tiket yang ingin dihapus: ", 1, len(tiket_files))
    if nomor_tiket is None:
        return

    tiket_file_path = os.path.join(folder_tiket, tiket_files[nomor_tiket - 1])
    os.remove(tiket_file_path)
    print(f"Tiket nomor {nomor_tiket} telah dihapus.")

def menu_pengunjung():
    while True:
        print(3 * "-", "Menu Pengunjung", 3 * "-")
        tampilkan_menu(["1. Lihat daftar film", "2. Beli tiket", "3. Kembali"])
        opsi = input("Pilih opsi (1/2/3): ")
        if opsi == "1":
            daftar_film()
        elif opsi == "2":
            beli_tiket()
        elif opsi == "3":
            break
        else:
            print("Input tidak valid.")

def daftar_film():
    print("Daftar film:")
    try:
        with open(file_name, "r") as file:
            nama_film = file.readlines()
        for index, line in enumerate(nama_film, start=1):
            print(f"{index}. {line.strip()}")
    except FileNotFoundError:
        print("Daftar film tidak ditemukan.")

def beli_tiket():
    print("Daftar film:")
    with open(file_name, "r") as file:
        nama_film = file.readlines()
    for index, line in enumerate(nama_film, start=1):
        print(f"{index}. {line.strip()}")
    print("0. Kembali")

    nomor_film = input_angka("Pilih nomor film yang ingin ditonton (atau 0 untuk kembali): ", 0, len(nama_film))
    if nomor_film == 0 or nomor_film is None:
        return

    film = nama_film[nomor_film - 1]
    tiket_id = buat_tiket()
    tiket_info = detail_tiket(film, tiket_id)
    simpan_tiket(tiket_info, tiket_id)
    print(f"Tiket berhasil dibuat dengan ID: {tiket_id}")

def buat_tiket():
    now = datetime.now()
    tiket_id = now.strftime("TICK%d%m%Y%H%M%S") + "!"
    return tiket_id

def detail_tiket(film, tiket_id):
    detail = f"""
    +-----------------------------------+
    |        TIKET BIOSKOP              |
    | ID TICKET: {tiket_id}   |
    | Film: {film.strip()}              |
    | Tanggal: {datetime.now()}|
    +-----------------------------------+
    |     Terimakasih telah membeli     |
    |            tiket anda             |
    +-----------------------------------+
    """
    return detail

def simpan_tiket(tiket_info, tiket_id):
    tiket_file_path = os.path.join(folder_tiket, f"{tiket_id}.txt")
    with open(tiket_file_path, "w") as file:
        file.write(tiket_info)
    print(f"Tiket disimpan di {tiket_file_path}.")

menu_utama()