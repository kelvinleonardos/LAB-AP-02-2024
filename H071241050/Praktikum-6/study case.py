
inventory = {}

def tambah_nomor():
    kode = input("Masukkan kode negara: ")
    nomor = int(input("Masukkan nomor (tidak perlu masukkan angka 0 pada awalan): "))
    
def tampilkan_kode():
    if not inventory:
        print("Tidak ada nomor yang di simpan.\n")
    else:
        print("kode negara dari nomor ini adalah:")
        for kode in inventory.items():
            print(f"{kode},")
        print()

def ganti_kode():
    kode = input("Masukkan kode negara yang ingin diganti: ")
    if kode in inventory:
        kode_baru = input("Masukkan kode negara baru: ")
        print(f"nomor dengan kode {kode_baru} berhasil diupdate!\n")
    else:
        print("Barang tidak ditemukan!\n")

def menu():
    while True:
        print("=== Aplikasi mengecek nomor telepon ===")
        print("1. Tambah nomor telepon")
        print("2. Tampilkan kode negara")
        print("3. mengganti kode negara")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            tambah_nomor()
        elif pilihan == "2":
            tampilkan_kode()
        elif pilihan == "3":
            ganti_kode()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan program inventory!")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih menu yang benar.\n")

menu()
