import json  
import os  

inventory_file = 'penyimpanan.json'  

def load_inventory():  
    if os.path.exists(inventory_file):  
        with open(inventory_file, 'r') as file:  
            return json.load(file)  
    return {}  

def save_inventory(inventory):  
    with open(inventory_file, 'w') as file:  
        json.dump(inventory, file, indent=4)  
 
inventory = load_inventory()  

def print_menu():  
    print("\nMenu Inventory Barang:")  
    print("1. Tambah Barang")  
    print("2. Hapus Barang")  
    print("3. Tampilkan Daftar Barang")  
    print("4. Cari Barang")  
    print("5. Update Data Barang")  
    print("6. Keluar")  

while True:  
    print_menu()  
    choice = input("Silakan masukkan pilihan Anda: ")  

    if choice == '1':  
        item_name = input("Silakan masukkan nama barang: ")  
        item_quantity = input("Silakan masukkan jumlah barang: ")  
        inventory[item_name] = item_quantity  
        save_inventory(inventory)  
        print(f"{item_name} telah ditambahkan dengan jumlah {item_quantity}.")  

    elif choice == '2':  
        item_name = input("Silakan masukkan nama barang yang ingin dihapus: ")  
        if item_name in inventory:  
            del inventory[item_name]  
            save_inventory(inventory)  
            print(f"{item_name} telah dihapus dari inventory.")  
        else:  
            print(f"{item_name} tidak ditemukan dalam inventory.")  

    elif choice == '3':  
        if inventory:  
            print("\nDaftar Barang:")  
            for name, quantity in inventory.items():  
                print(f"{name}: {quantity}")  
        else:  
            print("Inventory kosong.")  

    elif choice == '4':  
        item_name = input("Silakan masukkan nama barang yang ingin dicari: ")  
        if item_name in inventory:  
            print(f"{item_name} ditemukan dengan jumlah {inventory[item_name]}.")  
        else:  
            print(f"{item_name} tidak ditemukan dalam inventory.")  

    elif choice == '5':  
        item_name = input("Silakan masukkan nama barang yang ingin diperbarui: ")  
        if item_name in inventory:  
            new_quantity = input("Silakan masukkan jumlah baru barang: ")  
            inventory[item_name] = new_quantity  
            save_inventory(inventory)  
            print(f"{item_name} telah diperbarui menjadi {new_quantity}.")  
        else:  
            print(f"{item_name} tidak ditemukan dalam inventory.")  

    elif choice == '6':  
        print("Anda telah keluar dari program.")  
        break  

    else:  
        print("Maaf, pilihan yang Anda masukkan tidak tersedia. Silakan periksa kembali pilihan Anda.")