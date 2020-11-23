
import toga
from toga.style import Pack
from toga.style.pack import COLUMN


class MainWindow(toga.App):
    """Main window for wallpy

    """

    def startup(self):
        self.main_window = toga.MainWindow(title="Wallpy")

        box = toga.Box(style=Pack(direction=COLUMN))

        img = toga.Image(path="./images/jonatan-pie-3l3RwQdHRHg-unsplash.jpg")
        view = toga.ImageView(img)

        box.add(toga.Label("Bing image of the day"))
        box.add(view)

        self.main_window.content = box

        self.main_window.show()