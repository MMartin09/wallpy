import ctypes
import os
import platform


def set_wallpaper(file_name):
    if platform.system() == "Windows":
        file = os.path.abspath(file_name)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, file, 0)
    else:
        raise OSError("Error: Unsupported operating system!")
