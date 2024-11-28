from datetime import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []  # List untuk menyimpan tugas

    def tambah_tugas(self, nama_tugas, target_waktu):
        """
        Menambahkan tugas baru ke daftar.
        """
        try:
            deadline = datetime.strptime(target_waktu, "%Y-%m-%d %H:%M")
            self.tasks.append({"nama": nama_tugas, "target": deadline, "selesai": False})
            print(f"Tugas '{nama_tugas}' berhasil ditambahkan dengan target waktu {deadline}.")
        except ValueError:
            print("Format waktu salah. Gunakan format: YYYY-MM-DD HH:MM")

    def tampilkan_tugas(self):
        """
        Menampilkan semua tugas dalam daftar.
        """
        if not self.tasks:
            print("To-Do List kosong!")
            return
        
        print("\n=== Daftar Tugas ===")
        for i, task in enumerate(self.tasks, 1):
            status = "✅ Selesai" if task["selesai"] else "❌ Belum Selesai"
            deadline = task["target"].strftime("%Y-%m-%d %H:%M")
            print(f"{i}. {task['nama']} | Target: {deadline} | Status: {status}")
        print("====================")

    def tandai_selesai(self, nomor_tugas):
        """
        Menandai tugas tertentu sebagai selesai.
        """
        try:
            index = nomor_tugas - 1
            if 0 <= index < len(self.tasks):
                self.tasks[index]["selesai"] = True
                print(f"Tugas '{self.tasks[index]['nama']}' berhasil ditandai selesai.")
            else:
                print("Nomor tugas tidak valid.")
        except ValueError:
            print("Masukkan nomor tugas yang valid.")

    def hapus_tugas(self, nomor_tugas):
        """
        Menghapus tugas dari daftar.
        """
        try:
            index = nomor_tugas - 1
            if 0 <= index < len(self.tasks):
                removed_task = self.tasks.pop(index)
                print(f"Tugas '{removed_task['nama']}' berhasil dihapus.")
            else:
                print("Nomor tugas tidak valid.")
        except ValueError:
            print("Masukkan nomor tugas yang valid.")


def main():
    to_do_list = ToDoList()
    print("=== Sistem To-Do List ===")

    while True:
        print("\nPilih opsi:")
        print("1. Tambah tugas baru")
        print("2. Tampilkan daftar tugas")
        print("3. Tandai tugas sebagai selesai")
        print("4. Hapus tugas")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == "1":
            nama_tugas = input("Masukkan nama tugas: ").strip()
            target_waktu = input("Masukkan target waktu (YYYY-MM-DD HH:MM): ").strip()
            to_do_list.tambah_tugas(nama_tugas, target_waktu)

        elif pilihan == "2":
            to_do_list.tampilkan_tugas()

        elif pilihan == "3":
            try:
                nomor_tugas = int(input("Masukkan nomor tugas yang ingin ditandai selesai: "))
                to_do_list.tandai_selesai(nomor_tugas)
            except ValueError:
                print("Masukkan nomor tugas yang valid.")

        elif pilihan == "4":
            try:
                nomor_tugas = int(input("Masukkan nomor tugas yang ingin dihapus: "))
                to_do_list.hapus_tugas(nomor_tugas)
            except ValueError:
                print("Masukkan nomor tugas yang valid.")

        elif pilihan == "5":
            print("Keluar dari sistem. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
