
import toga

def test_window(widget):
    main_box = toga.Box()

    xx = toga.Label("Test Label")
    main_box.add(xx)

    new_window = toga.Window()
    new_window.content = main_box
    new_window.show()
