inventory = {}

def display_menu():  
    print("\nMenu Inventory Barang")  
    print("1. Tambah Barang")  
    print("2. Hapus Barang")  
    print("3. Tampilkan Daftar Barang")  
    print("4. Cari Barang")  
    print("5. Update Data Barang")  
    print("6. Keluar")  

def add_item():  
    item_code = input("Masukkan kode barang: ")  
    item_name = input("Masukkan nama barang: ")  
    item_quantity = int(input("Masukkan jumlah barang: "))  
    item_price = float(input("Masukkan harga barang: "))  
    inventory[item_code] = {'name': item_name, 'quantity': item_quantity, 'price': item_price}  
    print(f"Barang '{item_name}' dengan kode '{item_code}' berhasil ditambahkan.")  
    if item_quantity and item_price <= 0:
        print("Angka tidak valid")
def remove_item():  
    item_code = input("Masukkan kode barang yang ingin dihapus: ")  
    if item_code in inventory:  
        del inventory[item_code]  
        print(f"Barang dengan kode '{item_code}' berhasil dihapus.")  
    else:  
        print(f"Barang dengan kode '{item_code}' tidak ditemukan.")  

def display_items():  
    if inventory:  
        print("\nDaftar Barang:")  
        for item_code, details in inventory.items():  
            print(f"Kode: {item_code}, Nama: {details['name']}, Jumlah: {details['quantity']}, Harga: {details['price']}")  
    else:  
        print("Inventory kosong.")  

def search_item():  
    search_term = input("Masukkan kode atau nama barang yang ingin dicari: ")  
    found = False  
    for item_code, details in inventory.items():  
        if search_term == item_code or search_term.lower() == details['name'].lower():  
            print(f"Barang ditemukan: Kode = {item_code}, Nama = {details['name']}, Jumlah = {details['quantity']}, Harga = {details['price']}")  
            found = True  
            break  
    if not found:  
        print(f"Barang dengan kode atau nama '{search_term}' tidak ditemukan.")  

def update_item():  
    item_code = input("Masukkan kode barang yang ingin diupdate: ")  
    if item_code in inventory:  
        new_quantity = int(input("Masukkan jumlah baru: "))  
        new_price = float(input("Masukkan harga baru: "))  
        inventory[item_code]['quantity'] = new_quantity  
        inventory[item_code]['price'] = new_price  
        print(f"Barang dengan kode '{item_code}' berhasil diupdate.")  
    else:  
        print(f"Barang dengan kode '{item_code}' tidak ditemukan.")  

def main():  
    while True:  
        display_menu()  
        choice = input("Pilih opsi (1-6): ")  
        
        if choice == '1':  
            add_item()  
        elif choice == '2':  
            remove_item()  
        elif choice == '3':  
            display_items()  
        elif choice == '4':  
            search_item()  
        elif choice == '5':  
            update_item()  
        elif choice == '6':  
            print("Keluar dari program.")  
            break  
        else:  
            print("Pilihan tidak valid. Silakan coba lagi.")  

main()