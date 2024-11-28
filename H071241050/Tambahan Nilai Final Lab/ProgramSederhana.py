class DaftarBelanja:
    def __init__(self):  # Konstraktor untuk inisialisasi atribut (proses pengisian nilai)
        self.daftar = []  # Atribut berupa list kosong

    def tambah_item(self, item):
        if item not in self.daftar:
            self.daftar.append(item) #(operasi)
            print(f"{item} berhasil ditambahkan.")
        else:
            print(f"{item} sudah ada dalam daftar.")

    def tampilkan_daftar(self):
        if len(self.daftar) == 0: #
            print("Daftar belanja kosong.")
        else:
            print("Daftar belanja:")
            for i, item in enumerate(self.daftar, start=1):  # Looping untuk menampilkan daftar(penambahan indeks)
                print(f"{i}. {item}")

    def hapus_item(self, item):
        if item in self.daftar:
            self.daftar.remove(item) #
            print(f"{item} berhasil dihapus.")
        else:
            print(f"{item} tidak ditemukan dalam daftar.")

# Objek dari class
belanja = DaftarBelanja()

while True:
    print("\nMenu:")
    print("1. Tambah item")
    print("2. Tampilkan daftar")
    print("3. Hapus item")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        item = input("Masukkan nama item: ")
        belanja.tambah_item(item)
    elif pilihan == "2":
        belanja.tampilkan_daftar()
    elif pilihan == "3":
        item = input("Masukkan nama item yang akan dihapus: ")
        belanja.hapus_item(item)
    elif pilihan == "4":
        print("Program selesai. Selamat berbelanja!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")