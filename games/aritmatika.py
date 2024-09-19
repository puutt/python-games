import random
import main

def start():
    while True:
        simbol = random.choice(['+', '-', '*', '/'])
        angka1 = random.randint(1, 10)
        angka2 = random.randint(1, 10)

        jawaban = eval(f"{angka1} {simbol} {angka2}")

        while True:
            soal = int(input(f"\nBerapa hasil dari {angka1} {simbol} {angka2}? : "))
            
            if soal == jawaban:
                print(f"Kamu benar! Hasil dari {angka1} {simbol} {angka2} adalah {jawaban}")
            else:
                print(f"Salah! Hasil dari {angka1} {simbol} {angka2} adalah {jawaban}")
            break
    
        play_again = input("\nMau melanjutkan game-nya lagi? [Y/N]: ").lower()
        if play_again == "n":
            main.menu()
    
if __name__ == '__main__':
    start()