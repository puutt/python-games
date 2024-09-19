from libs import wlc_msg, exit_program
from games import mouseek
from games import aritmatika

def menu():
    user_option = int(input(f"\nMenu game: \n 1.Game MOUSEEK\n 2.Game ARITMATIKA\n 3.Keluar Program\n\nSilakan Pilih: "))
    
    if user_option == 1:
        mouseek.start()
    elif user_option == 2:
        aritmatika.start()
    elif user_option == 3:
        exit_program()
    else:
        print("Pilih game yang tersedia di menu")

def main():
    wlc_msg()
    menu()

if __name__ == '__main__':
    main()