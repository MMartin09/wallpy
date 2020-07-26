import requests
import wget

from wallpy.wallpaper import set_wallpaper


def main():
    wallpaper_file_1: str = "images/breno-machado-in9-n0JwgZ0-unsplash.jpg"
    wallpaper_file_2: str = "images/jonatan-pie-3l3RwQdHRHg-unsplash.jpg"

    set_wallpaper(wallpaper_file_2)

    r = requests.get('https://api.nasa.gov/planetary/apod?date=2020-07-25&api_key=DEMO_KEY')
    r = r.json()

    if r["media_type"] == "image":
        print(r["url"])
        wget.download(r["url"], out="image.jpg")


if __name__ == '__main__':
    main()
