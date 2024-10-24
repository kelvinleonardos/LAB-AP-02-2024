# Program Inventory Barang Sederhana
class BarangManager:
    def __init__(self):
        self.inventory = []  # List untuk menyimpan barang

    # Fungsi untuk menambah barang dengan pengecekan kode unik
    def tambah_barang(self):
        while True:
            try:
                kode_barang = int(input("Masukkan kode barang : "))
                # Cek apakah kode sudah ada
                if any(barang['kode'] == kode_barang for barang in self.inventory):
                    print(f"Kode {kode_barang} sudah ada, silakan masukkan kode yang berbeda.")
                else:
                    break  # Keluar dari loop jika kode unik
            except ValueError:
                print("Kode barang harus berupa angka, coba lagi.")

        barang = {
            "kode": kode_barang,  # Simpan kode yang telah diinput
            "nama": input("Masukkan nama barang : "),
            "jumlah": int(input("Masukkan jumlah barang : ")),
            "harga": float(input("Masukkan harga barang : "))
        }
        self.inventory.append(barang)  # Tambahkan barang ke dalam inventory
        print(f"Barang '{barang['nama']}' berhasil ditambahkan dengan kode {kode_barang}.")

    # Fungsi untuk menghapus barang
    def hapus_barang(self):
        pilihan = input("Pilih opsi (1 : Hapus semua, 2 : Hapus berdasarkan kode): ")
        if pilihan == '1':
            self.inventory.clear()
            print("Semua barang berhasil dihapus!\n")
        elif pilihan == '2':
            try:
                kode = int(input("Masukkan kode barang yang ingin dihapus : "))
                barang_dihapus = next((barang for barang in self.inventory if barang['kode'] == kode), None)
                if barang_dihapus:
                    self.inventory.remove(barang_dihapus)
                    print(f"Barang dengan kode '{kode}' berhasil dihapus!\n")
                else:
                    print(f"Barang dengan kode '{kode}' tidak ditemukan.\n")
            except ValueError:
                print("Kode barang harus berupa angka.")

    # Fungsi untuk menampilkan daftar barang
    def tampilkan_barang(self):
        if not self.inventory:
            print("Belum ada barang yang terdaftar.\n")
        else:
            print("Daftar Barang:")
            for barang in self.inventory:
                print(f"Barang dengan kode {barang['kode']} - Nama : {barang['nama']}, Jumlah : {barang['jumlah']}, Harga : {barang['harga']}")
            print()

    # Fungsi untuk mencari barang
    def cari_barang(self):
        try:
            kode = int(input("Masukkan kode barang yang ingin dicari : "))
            barang_ditemukan = next((barang for barang in self.inventory if barang['kode'] == kode), None)
            if barang_ditemukan:
                print(f"Barang ditemukan - Nama : {barang_ditemukan['nama']}, Jumlah : {barang_ditemukan['jumlah']}, Harga : {barang_ditemukan['harga']}\n")
            else:
                print(f"Barang dengan kode '{kode}' tidak ditemukan.\n")
        except ValueError:
            print("Kode barang harus berupa angka.")

    # Fungsi untuk mengupdate barang (jumlah & harga saja)
    def update_barang(self):
        try:
            kode = int(input("Masukkan kode barang yang ingin diupdate : "))
            barang_ditemukan = next((barang for barang in self.inventory if barang['kode'] == kode), None)
            if barang_ditemukan:
                barang_ditemukan['jumlah'] = int(input("Masukkan jumlah bar u: ") or barang_ditemukan['jumlah'])
                barang_ditemukan['harga'] = float(input("Masukkan harga baru : ") or barang_ditemukan['harga'])
                print(f"Barang dengan kode '{kode}' berhasil diupdate!\n")
            else:
                print(f"Barang dengan kode '{kode}' tidak ditemukan.\n")
        except ValueError:
            print("Kode barang harus berupa angka.")

# Fungsi untuk menampilkan menu
def menu():
    manager = BarangManager()  # Membuat instance dari BarangManager
    while True:
        pilihan = input(" Menu :\n 1. Tambah barang\n 2. Hapus barang\n 3. Tampilkan barang\n 4. Cari barang\n 5. Update barang\n 6. Keluar dari menu\nPilih menu : ")
        if pilihan == '1':
            manager.tambah_barang()
        elif pilihan == '2':
            manager.hapus_barang()
        elif pilihan == '3':
            manager.tampilkan_barang()
        elif pilihan == '4':
            manager.cari_barang()
        elif pilihan == '5':
            manager.update_barang()
        elif pilihan == '6':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!\n")

# Menjalankan program
if __name__ == "__main__":
    menu()



#  inventory = []

# # Fungsi untuk menambah barang
# def tambah_barang():
#     barang = {
#         "kode": input("Masukkan kode barang : "),
#         "nama": input("Masukkan nama barang : "),
#         "jumlah": int(input("Masukkan jumlah barang : ")),
#         "harga": float(input("Masukkan harga barang : "))
#     }
#     inventory.append(barang)
#     print(f"Barang '{barang['nama']}' berhasil ditambahkan!\n")

# # Fungsi untuk menghapus barang
# def hapus_barang():
#     pilihan = input("Pilih opsi (1 : Hapus semua, 2 : Hapus berdasarkan kode): ")
    
#     if pilihan == '1':
#         inventory.clear()
#         print("Semua barang berhasil dihapus!\n")
#     elif pilihan == '2':
#         kode = input("Masukkan kode barang yang ingin dihapus: ")
#         barang_dihapus = next((barang for barang in inventory if barang['kode'] == kode), None)
#         if barang_dihapus:
#             inventory.remove(barang_dihapus)
#             print(f"Barang dengan kode '{kode}' berhasil dihapus!\n")
#         else:
#             print(f"Barang dengan kode '{kode}' tidak ditemukan.\n")

# # Fungsi untuk menampilkan daftar barang
# def tampilkan_barang():
#     if not inventory:
#         print("Belum ada barang yang terdaftar.\n")
#     else:
#         print("Daftar Barang :")
#         for barang in inventory:
#             print(f"{barang['nama']} - Kode : {barang['kode']}, Jumlah : {barang['jumlah']}, Harga : {barang['harga']}")
#         print()

# # Fungsi untuk mencari barang
# def cari_barang():
#     kode = input("Masukkan kode barang yang ingin dicari: ")
#     barang_ditemukan = next((barang for barang in inventory if barang['kode'] == kode), None)
#     if barang_ditemukan:
#         print(f"Barang ditemukan : {barang_ditemukan}\n")
#     else:
#         print(f"Barang dengan kode '{kode}' tidak ditemukan.\n")

# # Fungsi untuk mengupdate barang (jumlah & harga saja)
# def update_barang():
#     kode = input("Masukkan kode barang yang ingin diupdate : ")
#     barang_ditemukan = next((barang for barang in inventory if barang['kode'] == kode), None)
#     if barang_ditemukan:
#         barang_ditemukan['jumlah'] = int(input("Masukkan jumlah baru : ") or barang_ditemukan['jumlah'])
#         barang_ditemukan['harga'] = float(input("Masukkan harga baru : ") or barang_ditemukan['harga'])
#         print(f"Barang dengan kode '{kode}' berhasil diupdate!\n")
#     else:
#         print(f"Barang dengan kode '{kode}' tidak ditemukan.\n")

# # Fungsi untuk menampilkan menu
# def menu():
#     while True:
#         pilihan = input("Menu :\n 1.Tambah barang\n 2.Hapus barang\n 3.Tampilkan barang\n 4.Cari barang\n 5.Update barang\n 6.Keluar dari menu\nPilih menu : ")
#         if pilihan == '1':
#             tambah_barang()
#         elif pilihan == '2':
#             hapus_barang()
#         elif pilihan == '3':
#             tampilkan_barang()
#         elif pilihan == '4':
#             cari_barang()
#         elif pilihan == '5':
#             update_barang()
#         elif pilihan == '6':
#             print("Terima kasih!")
#             break
#         else:
#             print("Pilihan tidak valid!\n")

# # Menjalankan program
# if __name__ == "__main__":
#     menu()
