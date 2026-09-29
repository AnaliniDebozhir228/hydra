import sys
import ctypes
import threading

MB_OK = 0x00000000
MB_ICONERROR = 0x00000010
MB_SYSTEMMODAL = 0x00001000
MB_SETFORGEGROUND = 0x00010000
MB_TOPMOST = 0x00040000

def show_sys_err():

    ctypes.windll.user32.MessageBoxW(0, "Произошла критическая ошибка. \nСистема может быть нестабильна.\n\nКод ошибки: 0xC0000005", "Ошибка",
                                     MB_OK | MB_ICONERROR | MB_SYSTEMMODAL | MB_SETFORGEGROUND | MB_TOPMOST)

    threading.Thread(target=show_sys_err, daemon=True).start()
    threading.Thread(target=show_sys_err, daemon=True).start()

if __name__ == '__main__':
    show_sys_err()