class ImageDownloader:
    def __init__(self):
        pass

    def download(self, target):
        if target == "apod":
            self._download_apod()
        elif target == "bing":
            self._download_bing()
        else:
            raise ValueError(target)

    def _download_apod(self):
        pass

    def _download_bing(self):
        pass
