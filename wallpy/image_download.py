import wget


class ImageDownload:
    def __init__(self):
        pass

    def download(self, url, file):
        wget.download(url, file)
