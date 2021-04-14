
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER


class MainWindow(toga.App):
    """Main window for wallpy

    """

    _imageview_apod: toga.ImageView
    _imageview_biod: toga.ImageView

    def startup(self):
        self.main_window = toga.MainWindow(title="Test")

        self.set_apod("./images/breno-machado-in9-n0JwgZ0-unsplash.jpg")
        self.set_biod("./images/jonatan-pie-3l3RwQdHRHg-unsplash.jpg")

        box_left = toga.Box(
            children=[
                toga.Label("Astronomy Picture of the Day"),
                self._imageview_apod,
            ],
            style=Pack(
                direction=COLUMN,
                padding_bottom=10,
                padding_left=10,
            )
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
            )
        )

        split = toga.SplitContainer()
        split.content = [(box_left, 0.5), (box_right, 0.5)]

        self.main_window.content = split

        self.main_window.show()

    def set_apod(self, path) -> None:
        self._imageview_apod = toga.ImageView(toga.Image(path))

    def set_biod(self, path) -> None:
        self._imageview_biod = toga.ImageView(toga.Image(path))
