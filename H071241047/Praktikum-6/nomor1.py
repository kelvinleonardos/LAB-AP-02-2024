gudang = {}
def tambah_barang():
    kode = int (input("Masukkan Kode Barang: "))
    nama = str( input("Masukkan Nama Barang: "))
    jumlah = int( input("Masukkan Jumlah: "))
    harga = int(input("Masukkka Harganya Perunit: "))
    gudang[kode] = {"nama":nama, "jumlah":jumlah, "harga":harga}

def hapus_barang():
    kode = int (input("Masukkkan Kode Barang: "))
    if kode in gudang:
        del gudang [kode]
        print(f"Barang dengan kode {kode} Telah Terhapus")
    else:
        print(f"Barang dengan kode {kode} Tidak Ditemukan")

def menampilkan_barang():
    if not gudang:
        print("Gudang kosong.")
    else:
        print("\nDaftar Barang:")
        for kode, barang in gudang.items():
            print(f"Kode: {kode}")
            for key, value in barang.items():
                print(f"{key.capitalize()}: {value}")
            print("-" * 20)

def cari_barang():
    kode = int(input("Masukkan kode barang yang ingin dicari: "))
    if kode in gudang:
        barang = gudang[kode]
        print(f"Barang ditemukan:")
        for key, value in barang.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("Barang tidak ditemukan.")

def mengupdate_data_barang():
    kode = int(input("Masukkan kode barang yang ingin diupdate: "))
    if kode in gudang:
        print("Pilih data yang ingin diupdate:")
        print("1. Nama")
        print("2. Jumlah")
        print("3. Harga")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == '1':
            nama_baru = str(input("Masukkan nama baru: "))
            gudang[kode]['nama'] = nama_baru
        elif pilihan == '2':
            jumlah_baru = int(input("Masukkan jumlah baru: "))
            gudang[kode]['jumlah'] = jumlah_baru
        elif pilihan == '3':
            harga_baru = float(input("Masukkan harga baru: "))
            gudang[kode]['harga'] = harga_baru
        else:
            print("Pilihan tidak valid.")
        print("Data barang berhasil diupdate.")

while True:
    print("\nMenu:")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Daftar Barang")
    print("4. Cari Barang")
    print("5. Update Data Barang")
    print("6. Keluar")

    pilihan = input("Masukkan pilihan: ")
    if pilihan == '1':
        tambah_barang()
    elif pilihan == '2':
        hapus_barang()
    elif pilihan == '3':
        menampilkan_barang()
    elif pilihan == '4':
        cari_barang()
    elif pilihan == '5':
        mengupdate_data_barang()
    elif pilihan == '6':
        break
    else:
        print("Pilihan tidak valid.")