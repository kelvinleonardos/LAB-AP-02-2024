inventory = {}

def tampilkan_menu():
    print("\n=== Menu inventory Barang ===")
    print("1. Tambahkan Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Daftar Barang")
    print("4. Cari Barang")
    print("5. Update Data Barang")
    print("6. Keluar")

def tambah_barang():
    kode_barang   = input("Masukkan kode barang: ")
    nama_barang   = input("Masukkan Nama Barang: ")
    jumlah_barang = int(input("Masukkan Jumlah Barang: "))
    harga         = float(input("Masukkan Jumlah barang: "))
    inventory[kode_barang] = {'nama': nama_barang, 'jumlah': jumlah_barang, 'harga': harga}
    print(f"Barang '{nama_barang}' berhasil di tambahkan.")

def hapus_barang():
    kode_barang = input("Masukkan Kode Barang yang ingin Anda Hapus: ")
    if kode_barang in inventory:
        del inventory[kode_barang]
        print("Barang Berhasil Dihapus.")
    else:
        print("Kode atau Nama barang Tidak Dalam inventory")

def tampilkan_barang():
    if not inventory:
        print("Tidak ada barang dalam inventory.")
    else:
        print("\nDaftar Barang:")
        for kode, info in inventory.items():
            print(f"Kode: {kode}, Nama: {info['nama']}, Jumlah: {info['jumlah']}, Harga: {info['harga']}")

def cari_barang():
    kode_barang = input("Masukkan Kode Barang yang Anda Ingin Cari: ")
    if kode_barang in inventory:
        info = inventory[kode_barang]
        print(f"Barang ditemukan - kode: {kode_barang}, Nama: {info['nama']}, jumlah: {info['jumlah']}, harga: {info['harga']}")
    else:
        print("Barang yang Anda Cari tidak ditemukan.")

def update_barang():
    kode_barang = input("Masukkan Kode Barang yang Ingin Anda Perbarui: ")
    if kode_barang in inventory:
        nama_barang   = input("Masukkan Nama Baru: ")
        jumlah_barang = int(input("Masukkan Jumlah Baru: "))
        harga         = float(input("Masukkan Harga Baru: "))
        inventory[kode_barang] = {'nama': nama_barang, 'jumlah': jumlah_barang, 'harga': harga }
        print("Data Barang Berhasil Diperbarui")
    else:
        print("Kode Barang Tidak Ditemukan")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            hapus_barang()
        elif pilihan == '3':
            tampilkan_barang()
        elif pilihan == '4':
            cari_barang()
        elif pilihan == '5':
            update_barang()
        elif pilihan == '6':
            print("Terima Kasih :) Program Selesai.")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")
main()

            





