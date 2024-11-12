import os
from datetime import datetime

nama_folder = 'film'
daftar_film = os.path.join(nama_folder, 'daftar_film.txt')
nama_folder2 = 'tiket'

def folder_tiket():
    os.makedirs(nama_folder2, exist_ok=True)

def folder_film():
    os.makedirs(nama_folder, exist_ok=True)

def load_film():
    if not os.path.exists(daftar_film):
        return []
    with open(daftar_film, 'r') as file:
        return [line.strip() for line in file.readlines()]

def save_film(film):
    with open(daftar_film, 'a') as file:
        file.write(film + '\n')

def hapus_film(film_index):
    film = load_film()
    if 1 <= film_index <= len(film):
        del film[film_index - 1]
        with open(daftar_film, 'w') as file:
            for f in film:
                file.write(f + '\n')
        print("Film berhasil dihapus.")
    else:
        print("Film yang dipilih tidak valid.")

def tampilkan_daftar_film():
    film = load_film()
    print("Daftar Film:")
    for i, f in enumerate(film):
        print(f"{i + 1}. {f}")

def tambah_film():
    nama_film = input("Masukkan nama film: ")
    film_info = nama_film
    save_film(film_info)
    print("Film berhasil ditambahkan!")

def buat_id_tiket():
    return f"TICK{datetime.now().strftime('%d%m%Y%H%M%S')}"

def format_info_tiket(id_tiket, film):
    return (f"+---------------------------------+\n"
            f"|           TIKET BIOSKOP         |\n"
            f"+---------------------------------+\n"
            f"| ID Tiket : {id_tiket}           |\n"
            f"| Film     : {film}               |\n"
            f"| Tanggal  : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')} |\n"
            f"+---------------------------------+\n"
            f"|    Terima kasih telah membeli   |\n"
            f"|            tiket Anda!          |\n"
            f"+---------------------------------+")

def beli_tiket(film_pilihan):
    film = load_film()
    if 1 <= film_pilihan <= len(film):
        film_terpilih = film[film_pilihan - 1]
        id_tiket = buat_id_tiket()
        tiket_info = format_info_tiket(id_tiket, film_terpilih)

        folder_tiket()
        with open(os.path.join(nama_folder2, f"{id_tiket}.txt"), 'w') as file:
            file.write(tiket_info)
        print(f"Tiket berhasil dibeli! Simpan di: {id_tiket}.txt")
    else:
        print("Film yang dipilih tidak valid.")

def load_tiket():
    if not os.path.exists(nama_folder2):
        print("Folder tiket tidak ditemukan.")
        return []
    
    return [(file, open(os.path.join(nama_folder2, file)).read().strip()) for file in os.listdir(nama_folder2) if file.endswith('.txt')]

def tampilkan_daftar_tiket():
    tiket_list = load_tiket()
    print("Daftar Tiket:")
    for i, (file, _) in enumerate(tiket_list):
        print(f"{i + 1}. {file}")

def tampilkan_detail_tiket(tiket_index):
    tiket_list = load_tiket()
    if 1 <= tiket_index <= len(tiket_list):
        print("Detail Tiket:")
        print(tiket_list[tiket_index - 1][1])
    else:           
        print("Tiket yang dipilih tidak valid.")

def hapus_tiket(tiket_index):
    tiket_list = load_tiket()
    if 1 <= tiket_index <= len(tiket_list):
        os.remove(os.path.join(nama_folder2, tiket_list[tiket_index - 1][0]))
        print("Tiket berhasil dihapus.")
    else:
        print("Tiket yang dipilih tidak valid.")

def menu_daftar_tiket():
    while True:
        print("\n=== Menu Daftar Tiket ===")
        print("1. Tampilkan Daftar Tiket")
        print("2. Lihat Detail Tiket")
        print("3. Hapus Tiket")
        print("0. Kembali ke Menu Admin")

        pilihan = input("Pilih opsi: ")
        if pilihan == '0':
            break
        elif pilihan == '1':
            tampilkan_daftar_tiket()
        elif pilihan == '2':
            tampilkan_daftar_tiket()
            try:
                tiket_index = int(input("Pilih tiket untuk melihat detail (nomor): "))
                tampilkan_detail_tiket(tiket_index)
            except ValueError:
                print("Input tidak valid.")
        elif pilihan == '3':
            tampilkan_daftar_tiket()
            try:
                tiket_index = int(input("Pilih tiket untuk dihapus (nomor): "))
                hapus_tiket(tiket_index)
            except ValueError:
                print("Input tidak valid.")
        else:
            print("Opsi tidak valid.")

def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Tambah Film")
        print("2. Hapus Film")
        print("3. Tampilkan Daftar Film")
        print("4. Daftar Tiket")
        print("0. Untuk kembali")

        pilihan = input("Pilih opsi: ")
        if pilihan == '0':
            break
        elif pilihan == '1':
            tambah_film()
        elif pilihan == '2':
            tampilkan_daftar_film()
            try:
                film_index = int(input("Pilih film untuk dihapus (nomor): "))
                hapus_film(film_index)
            except ValueError:
                print("Input tidak valid.")
        elif pilihan == '3':
            tampilkan_daftar_film()
        elif pilihan == '4':
            menu_daftar_tiket()
        else:
            print("Opsi tidak valid.")

def menu_pengunjung():
    while True:
        print("\n=== Menu Pengunjung ===")
        print("1. Tampilkan Daftar Film")
        print("2. Beli Tiket")
        print("3. Tampilkan Daftar Tiket")
        print("0. Kembali ke Menu Utama")
        
        pilihan = input("Pilih opsi: ")
        if pilihan == '0':
            break
        elif pilihan == '1':
            tampilkan_daftar_film()
        elif pilihan == '2':
            tampilkan_daftar_film()
            try:
                film_pilihan = int(input("Pilih film untuk beli tiket (nomor): "))
                beli_tiket(film_pilihan)
            except ValueError:
                print("Input tidak valid.")
        elif pilihan == '3':
            tampilkan_daftar_tiket()
        else:
            print("Opsi tidak valid.")

def main():
    folder_film()  
    while True:
        print("\n=== Menu Utama ===")
        print("1. Menu Admin")
        print("2. Menu Pengunjung")
        print("0. Keluar")

        pilihan = input("Pilih opsi: ")
        if pilihan == '0':
            print("Terima kasih!")
            break
        elif pilihan == '1':
            menu_admin()
        elif pilihan == '2':
            menu_pengunjung()
        else:
            print("Opsi tidak valid.")

main()
