#TP4_1_H071241020
import random

# Dek kartu dengan nilai Blackjack (Ace = 11, kartu wajah = 10)
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Fungsi untuk menarik kartu acak dari dek
def draw_card():
    return random.choice(cards)  # Mengambil kartu acak setiap kali dipanggil

# Fungsi untuk menghitung total kartu
def calculate_hand_value(hand):
    total = sum(hand)
    ace_count = hand.count(11)
    # Jika ada Ace (11) dan total lebih dari 21, ubah nilai Ace menjadi 1
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total

# Fungsi utama untuk permainan Blackjack
def blackjack():
    print("Welcome to Blackjack!")
    
    # Kartu awal pemain dan dealer
    player_hand = [draw_card()]
    dealer_hand = [draw_card()]

    print(f"Kartu Anda sekarang adalah: {player_hand}")
    print(f"Kartu dealer adalah: {dealer_hand[0]}")

    # Pemain mengambil kartu
    while True:
        choice = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
        if choice == 'y':
            player_hand.append(draw_card())
            player_total = calculate_hand_value(player_hand)
            print(f"Kartu Anda sekarang adalah: {player_hand} (Total: {player_total})")
            
            # Jika total nilai kartu pemain melebihi 21, pemain kalah
            if player_total > 21:
                print("Anda kalah, kartu anda melebihi 21.")
                return
        elif choice == 'n':
            break
        else:
            print("Input tidak valid, silakan masukkan 'y' untuk yes atau 'n' untuk no.")
    
    # Dealer menarik kartu hingga totalnya mencapai 17 atau lebih
    print(f"Kartu dealer sekarang adalah: {dealer_hand}")
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(draw_card())
        print(f"Kartu dealer sekarang adalah: {dealer_hand} (Total: {calculate_hand_value(dealer_hand)})")

    # Menghitung nilai akhir pemain dan dealer
    player_total = calculate_hand_value(player_hand)
    dealer_total = calculate_hand_value(dealer_hand)

    # Menentukan hasil akhir permainan
    if dealer_total > 21:
        print("Anda menang, dealer melebihi 21.")
    elif player_total > dealer_total:
        print("Anda menang!")
    elif player_total == dealer_total:
        print("Seri!")
    else:
        print("Dealer menang!")

# Jalankan permainan Blackjack
blackjack()

