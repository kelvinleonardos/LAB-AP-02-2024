def tampilkan_menu():
    print("\n=== Menu ===")
    print("1. Tambahkan Tugas")
    print("2. Lihat Semua Tugas")
    print("3. Cari Tugas")
    print("4. Hapus Tugas")
    print("5. Keluar")

def tambahkan_tugas(daftar_tugas):
    tugas = input("Masukkan deskripsi tugas: ").strip()
    if tugas:  
        daftar_tugas.append(tugas)
        print(f"Tugas '{tugas}' berhasil ditambahkan!")
    else:
        print("Deskripsi tugas tidak boleh kosong!")

def lihat_tugas(daftar_tugas):
    if daftar_tugas:
        print("\nDaftar Tugas:")
        for i, tugas in enumerate(daftar_tugas, start=1):
            print(f"{i}. {tugas}")
    else:
        print("\nTidak ada tugas dalam daftar.")

def cari_tugas(daftar_tugas):
    kata_kunci = input("Masukkan kata kunci pencarian: ").strip()
    hasil_cari = [tugas for tugas in daftar_tugas if kata_kunci.lower() in tugas.lower()]
    if hasil_cari:
        print("\nHasil Pencarian:")
        for tugas in hasil_cari:
            print(f"- {tugas}")
    else:
        print("Tidak ada tugas yang sesuai dengan kata kunci.")

def hapus_tugas(daftar_tugas):
    lihat_tugas(daftar_tugas)
    try:
        nomor = int(input("\nMasukkan nomor tugas yang ingin dihapus: "))
        if 1 <= nomor <= len(daftar_tugas):
            tugas_hapus = daftar_tugas.pop(nomor - 1)
            print(f"Tugas '{tugas_hapus}' berhasil dihapus!")
        else:
            print("Nomor tugas tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")

def main():
    daftar_tugas = [] 
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == "1":
            tambahkan_tugas(daftar_tugas)
        elif pilihan == "2":
            lihat_tugas(daftar_tugas)
        elif pilihan == "3":
            cari_tugas(daftar_tugas)
        elif pilihan == "4":
            hapus_tugas(daftar_tugas)
        elif pilihan == "5":
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


main()