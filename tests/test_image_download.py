import tempfile
import os
import pytest

from urllib.error import URLError

from wallpy.image_download import ImageDownload


class TestImageDownload:

    image_download = ImageDownload()

    fp = tempfile.TemporaryDirectory()
    file = os.path.join(fp.name, "wallpaper.jpg")

    def test_download(self):
        self.image_download.download(
            "https://jsonplaceholder.typicode.com/users/1/todos", self.file
        )

    def test_download_invalid_url(self):
        with pytest.raises(OSError):
            self.image_download.download(
                "https://jsonplaceholder.typicode.co", self.file
            )
