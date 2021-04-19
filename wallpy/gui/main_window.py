import tempfile
import os
import time
from urllib.error import URLError
import threading

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER

from wallpy.url_query import UrlQuery
from wallpy.image_download import ImageDownload
from wallpy.notification import notificate

from wallpy.gui.test_window import test_window


class MainWindow(toga.App):
    """Main window for wallpy"""

    _imageview_apod: toga.ImageView
    _imageview_biod: toga.ImageView

    def startup(self):
        self.main_window = toga.MainWindow(title="Wallpy")

        self._imageview_apod = toga.ImageView()
        self._imageview_biod = toga.ImageView()

        self.set_apod("./images/breno-machado-in9-n0JwgZ0-unsplash.jpg")
        self.set_biod("./images/breno-machado-in9-n0JwgZ0-unsplash.jpg")

        things = toga.Group('Edit')
        cmd0 = toga.Command(
            self.test,
            label='Action 0',
            tooltip='Perform action 0',
            group=things
        )

        self.commands.add(cmd0)

        box_left = toga.Box(
            children=[
                toga.Label("Astronomy Picture of the Day"),
                self._imageview_apod,
            ],
            style=Pack(
                direction=COLUMN,
                padding_bottom=10,
                padding_left=10,
            ),
        )

        box_right = toga.Box(
            children=[
                toga.Label("Bing image of the day"),
                self._imageview_biod,
            ],
            style=Pack(
                direction=COLUMN,
                padding_bottom=10,
                padding_left=10,
                padding_right=10,
            ),
        )

        split = toga.SplitContainer()
        split.content = [(box_left, 0.5), (box_right, 0.5)]

        self.main_window.content = split
        self.main_window.show()

        fp = tempfile.gettempdir()
        file_apod = os.path.join(fp, "apod.jpg")
        file_biod = os.path.join(fp, "biod.jpg")

        x = threading.Thread(target=self.thread_function, args=(file_apod, file_biod))
        x.start()

    def test(self, widget):
        test_window(widget)

    def thread_function(self, file_apod, file_biod):
        url_apod = UrlQuery().query("apod")
        url_biod = UrlQuery().query("bing")

        try:
            ImageDownload().download(url_apod, file_apod)
            self.set_apod(file_apod)
        except URLError:
            print("Could not download the image")
            # TODO Handle error (Maybe display temp image!)

        try:
            ImageDownload().download(url_biod, file_biod)
            self.set_biod(file_biod)
        except URLError:
            print("Could not download the image")
            # TODO Handle error (Maybe display temp image!)

        notificate("Image download", "Successfully downloaded APoD and BIoD!")

    def set_apod(self, path) -> None:
        """Load the APoD and display it.

        Args:
            path (str): Path to the APoD image

        """

        image = toga.Image(path)
        self._imageview_apod.image = image

    def set_biod(self, path) -> None:
        """Load the BIoD and display it.

        Args:
            path (str): Path to the BIoD image

        """

        image = toga.Image(path)
        self._imageview_biod.image = image
