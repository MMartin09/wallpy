import requests
import wget

from wallpy.wallpaper import set_wallpaper
from wallpy.apod_downloader import download_apod


def main():
    # wallpaper_file_1: str = "images/breno-machado-in9-n0JwgZ0-unsplash.jpg"
    # wallpaper_file_2: str = "images/jonatan-pie-3l3RwQdHRHg-unsplash.jpg"

    # set_wallpaper(wallpaper_file_2)

    download_apod("test.jpg")


if __name__ == '__main__':
    main()
