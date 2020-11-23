
import toga


class MainWindow(toga.App):
    """Main window for wallpy

    """

    def startup(self):
        self.main_window = toga.MainWindow(title="Wallpy")

        box = toga.Box()
        button = toga.Button('Hello world')
        button.style.padding = 50
        button.style.flex = 1
        box.add(button)

        self.main_window.content = box

        self.main_window.show()