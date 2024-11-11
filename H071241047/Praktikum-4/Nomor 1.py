import random

def ambil_kartu(kartu):
    return kartu.pop()

def hitung_skor(tangan):
    return sum(tangan)

def giliran_pemain(kartu):
    tangan_pemain = [ambil_kartu(kartu)]
    print("Welcome to Blackjack!")
    print(f"Kartu anda sekarang adalah: {tangan_pemain[0]}")

    while True:
        pilihan = input("Apakah masih akan mengambil kartu? (ya/no) ").lower()
        if pilihan == 'ya':
            tangan_pemain.append(ambil_kartu(kartu))
            skor_pemain = hitung_skor(tangan_pemain)
            print(f"Kartu anda sekarang adalah: {skor_pemain}")
            if skor_pemain > 21:
                print("Anda kalah, kartu anda melebihi 21.")
                return None
        elif pilihan == 'no':
            break
    return tangan_pemain

def giliran_dealer(kartu):
    tangan_dealer = [ambil_kartu(kartu)]
    print(f"Kartu dealer adalah: {tangan_dealer[0]}")

    while hitung_skor(tangan_dealer) < 17:
        tangan_dealer.append(ambil_kartu(kartu))
        print(f"Kartu dealer sekarang adalah: {hitung_skor(tangan_dealer)}")

    return tangan_dealer

def blackjack():
    kartu = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(kartu)

    # Giliran pemain
    tangan_pemain = giliran_pemain(kartu)
    if tangan_pemain is None:
        return

    # Giliran dealer
    tangan_dealer = giliran_dealer(kartu)

    # Menentukan pemenang
    skor_pemain = hitung_skor(tangan_pemain)
    skor_dealer = hitung_skor(tangan_dealer)

    if skor_dealer > 21:
        print("Anda menang, dealer melebihi 21.")
    elif skor_pemain > skor_dealer:
        print("Anda menang!")
    elif skor_pemain == skor_dealer:
        print("Seri!")
    else:
        print("Dealer menang!")

blackjack()