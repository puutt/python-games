import socket
from time import sleep

PC_NAME = socket.gethostname()

def wlc_msg():
    style = "*" * (len(PC_NAME) + 6)
    print(style)
    print(f"** {PC_NAME} **")
    print(style)
    
def exit_program():
    print('Program akan dihentikan')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Program berhasil dihentikan')

if __name__ == '__main__':
    wlc_msg()
    exit_program()