import os
from datetime import datetime
file_name = "FILM.txt"
folder_tiket = "TIKET TA ADA DISINI"
os.makedirs(folder_tiket, exist_ok=True)
def menu_utama():
    while True:
        print("=== Sistem Pemesanan Tiket Bioskop ===")
        A = ["1. Admin", "2. Pengunjung", "3. Keluar"]
        for i in A:
            print(i)
        peran = input("Pilih ingin jadi apa, yang penting jangan presiden (1/2/3): ")
        if peran == "1":
            menu_admin()
        elif peran == "2":
            menu_pengunjung()
        elif peran == "3":
            print("Kapan kapan kesini ki lagi nah")
            break
        else:
            print("Silahkan pilih angka 1 sampai 3")
def menu_admin():    
    while True:
        print("=== Menu Admin ===")
        A = ["1. Tambah film", "2. Hapus film", "3. Daftar Tiket", "4. Kembali"]
        for j in A:
            print(j)
        opsi = input("Pilih maki (1/2/3/4): ")

        if opsi == "1":
            tambah_film()
        elif opsi == "2":
            hapus_film()
        elif opsi == "3":
            daftar_tiket()
        elif opsi == "4":
            break
        else:
            print("Silahkan pilih angka 1 sampai 4")

def tambah_film():
    print("=== Tambah Film ===")
    film = input("Masukkan nama film yang ingin ditambahkan (atau tekan enter untuk kembali): ")
    if film: 
        with open(file_name, "a") as file:
            file.write(film + "\n")
        print(f"Film '{film}' ditambahkan ke file {file_name}.")
    else:
        print("Input film kosong, kembali ke menu.")

def hapus_film():
    print("=== Hapus Film ===")
    print("Daftar Film:")
    
    with open(file_name, "r") as file:
        nama_film = file.readlines()  # Membuat list dari file daftar film
    for index, line in enumerate(nama_film, start=1):
        print(f"{index}. {line.strip()}")

    try:
        nomor_baris = int(input("Pilihki film keberapa yang mau kita hapus (atau 0 untuk kembali): "))
        if nomor_baris == 0:
            print("Kembali ke menu.")
            return
        if 1 <= nomor_baris <= len(nama_film):
            del nama_film[nomor_baris - 1]

            with open(file_name, "w") as file:
                file.writelines(nama_film)
            print("Film telah dihapus")
        else:
            print("Nomor baris tidak valid.")

    except ValueError:
        print("Input tidak valid. Harap masukkan angka untuk nomor film.")

def daftar_tiket():
    while True:
        print("=== Daftar Tiket ===")
        B = ["1. Lihat Daftar Tiket", "2. Lihat Detail Tiket", "3. Hapus Tiket", "4. Kembali"]
        for a in B:
            print(a)
        opsi = input("Pilih maki (1/2/3/4): ")

        if opsi == "1":
            lihat_daftar_tiket()
        elif opsi == "2":
            lihat_detail_tiket()
        elif opsi == "3":
            hapus_tiket()
        elif opsi == "4":
            break
        else:
            print("Silahkan pilih angka 1 sampai 4")

def lihat_daftar_tiket():
    print("Daftar tiket:")
    try:
        tiket_files = os.listdir(folder_tiket)       
        
        if not tiket_files:
            print("Tidak ada tiket yang tersedia.")
        else:
            for index, id_tiket in enumerate(tiket_files, start=1):
                print(f"{index}. {id_tiket}")
    except Exception as e:
        print(f"Error! Tidak dapat membaca daftar tiket: {e}")

def lihat_detail_tiket():
    tiket_files = os.listdir(folder_tiket)
    for index, id_tiket in enumerate(tiket_files, start=1):
        print(f"{index}. {id_tiket}")
    try:
        
        nomor_tiket = int(input("Masukkan nomor tiket yang ingin dilihat detailnya: "))
        file_tiket = os.listdir(folder_tiket)  # Membuat list berdasarkan nama file yang ada di folder
        
        if 1 <= nomor_tiket <= len(file_tiket):
            tiket_file_path = os.path.join(folder_tiket, file_tiket[nomor_tiket - 1])
            with open(tiket_file_path, "r") as file:
                detail_tiket = file.read()
            print(f"Detail Tiket:\n{detail_tiket}")
        else:
            print(f"Tiket dengan nomor tiket {nomor_tiket} tidak ditemukan.")
    
    except ValueError:
        print("Input tidak valid. Harap masukkan angka untuk nomor tiket.")

def hapus_tiket():
    tiket_files = os.listdir(folder_tiket)
    for index, id_tiket in enumerate(tiket_files, start=1):
        print(f"{index}. {id_tiket}")
    try:
        nomor_tiket = int(input("Masukkan nomor keberapa tiket yang mau kita hapus (tekanki 0 untuk kembali):"))
        file_tiket = os.listdir(folder_tiket)
        
        if nomor_tiket == 0:
            print("Kembali ke menu.")
            return
        if 1 <= nomor_tiket <= len(file_tiket):
            tiket_file_path = os.path.join(folder_tiket, file_tiket[nomor_tiket - 1])
            os.remove(tiket_file_path)
            print(f"Tiket nomor {nomor_tiket} telah dihapus.")
        else:
            print("Nomor tiket tidak valid.")
    
    except ValueError:
        print("Input tidak valid. Harap masukkan angka untuk nomor tiket.")

def menu_pengunjung():
    while True:
        print("=== Menu Pengunjung ===")
        C = ["1. Lihat daftar film", "2. Beli tiket", "3. Kembali"]
        for j in C:
            print(j)
        opsi = input("Pilih maki kak (1/2/3): ")

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

    except Exception as e:
        print(f"Error! Daftar film tidak ditemukan: {e}")

def beli_tiket():
    print("Daftar film:")
    with open(file_name, "r") as file:
        nama_film = file.readlines()
    
    for index, line in enumerate(nama_film, start=1):
        print(f"{index}. {line.strip()}")
    print("0. Kembali")

    try:
        nomor_film = int(input("Pilih nomor film yang ingin ditonton (atau 0 untuk kembali): "))
        if nomor_film == 0:
            return
        if 1 <= nomor_film <= len(nama_film):
            film = nama_film[nomor_film - 1]
            tiket_id = buat_tiket()
            tiket_info = detail_tiket(film, tiket_id)
            simpan_tiket(tiket_info, tiket_id)
            print(f"Tiket berhasil dibuat dengan ID: {tiket_id}")
        else:
            print(f"Nomor film {nomor_film} tidak ditemukan")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka untuk nomor film.")

def buat_tiket():
    now = datetime.now()
    tiket_id = now.strftime("TICK%d%m%Y%H%M%S") + "!"
    return tiket_id

def detail_tiket(film, tiket_id):
    lebar_kotak = 111  # Lebar kotak, sesuai jumlah karakter pada garis horizontal
    pesan_terima_kasih = "Terimakasih telah membeli tiket kami"

    # Menghitung posisi tengah untuk pesan "Terimakasih telah membeli tiket kami"
    padding_kiri = (lebar_kotak - len(pesan_terima_kasih)) // 2
    spasi_kiri = " " * padding_kiri

    detail = f"""
    +---------------------------------------------------------------------------------------------------------------+
                                                     TIKET BIOSKOP                                                                                          
     ID TICKET: {tiket_id}                                                                                         
     Film: {film}                                                                                                  
     Tanggal: {datetime.now()}                                                                                                                      
    +---------------------------------------------------------------------------------------------------------------+
    |{spasi_kiri}{pesan_terima_kasih}{' ' * (lebar_kotak - len(spasi_kiri) - len(pesan_terima_kasih))}|
    +---------------------------------------------------------------------------------------------------------------+
    """
    print(detail)
    return detail


def simpan_tiket(tiket_info, tiket_id):
    try:
        tiket_file_path = os.path.join(folder_tiket, f"{tiket_id}.txt")
        with open(tiket_file_path, "w") as file:
            file.write(tiket_info)
        print(f"Tiket disimpan di {tiket_file_path}.")
    except Exception as e:
        print(f"Error! Tidak dapat menyimpan tiket: {e}")
menu_utama()    