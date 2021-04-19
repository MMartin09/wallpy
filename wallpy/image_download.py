import wget
import shutil
from urllib import request
import os


class ImageDownload:
    def __init__(self):
        pass

    def download(self, url, file):
        if os.path.exists(file):
            os.remove(file)

        filename, _ = request.urlretrieve(url, file)
