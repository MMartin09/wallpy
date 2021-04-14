import wget
import shutil
from urllib import request
import os


class ImageDownload:
    def __init__(self):
        pass

    def download(self, url, file):
        target_dir = os.path.dirname(file)
        filename, _ = request.urlretrieve(url, target_dir)

        if os.path.exists(file):
            os.remove(file)

        #os.rename(filename, file)

        return filename

