import random

def ambilKartu():
    return random.randint(1, 10)

def giliranPemain():
    kartuPemain = ambilKartu()
    print("Kartu anda sekarang adalah: " + str(kartuPemain))

    while True:
        print("Apakah masih akan mengambil kartu? (y/n)")
        if input().lower() != 'y':
            break
        kartuPemain += ambilKartu()
        print(f"Kartu anda sekarang adalah: {kartuPemain}")
        if kartuPemain > 21:
            print("Anda kalah!")
            return kartuPemain

    return kartuPemain

def giliranDealer():
    kartuDealer = ambilKartu()
    print("Kartu dealer adalah: " + str(kartuDealer))

    while kartuDealer < 17:
        kartuDealer += ambilKartu()
        print("Kartu dealer sekarang adalah: " + str(kartuDealer))

    if kartuDealer > 21:
        print("Dealer kalah!")

    return kartuDealer

def cekPemenang(kartuPemain, kartuDealer):
    if kartuPemain > 21:
        print("Anda kalah, kartu anda melebihi 21.")
    elif kartuDealer > 21:
        print("Anda menang, dealer melebihi 21.")
    elif kartuPemain > kartuDealer:
        print("Anda menang!")
    elif kartuPemain == kartuDealer:
        print("Seri!")
    else:
        print("Dealer menang!")

def main():
    print("Welcome to Blackjack!")

    kartuPemain =giliranPemain()

    if kartuPemain <= 21:
        kartuDealer = giliranDealer()
        cekPemenang(kartuPemain, kartuDealer)

main()