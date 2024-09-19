import random 
import main

def start():
    while True:
        tikus_position = random.randint(1, 4) 
        goa_kosong = ["|_|"] * 4
        goa = goa_kosong.copy()

        goa[tikus_position - 1] = "|0^0|" 

        print(f'\nCoba perhatikan lubang dibawah ini\n\n{' '.join(goa_kosong)}\n')

        while True:
            try:

                pilihan_user = int(input("Menurut kamu, di lubang nomor berapa Tikus berada? [1 / 2 / 3 / 4]: "))
                if pilihan_user not in [1, 2, 3, 4]:
                    print("Pilihan harus antara 1 sampai 4!")
                    continue
            except ValueError:
                print("Masukkan angka yang benar!")
                continue

            if pilihan_user == tikus_position:
                print(f"\n{'  '.join(goa)}\nSelamat kamu menang 🏆 ")
            else:
                print(f"\n{'  '.join(goa)},\nYah kamu kalah ☹️ ")
            break
                
        play_again = input("\nMau melanjutkan game-nya lagi? [Y/N]: ").lower()
        if play_again == "n":
            main.menu()
    
if __name__ == '__main__':
    start()