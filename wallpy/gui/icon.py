"""
Functions to get the path of the icon file.

The icon is "Framed Picture" from `Microsoft Emojis`_.

.. _Microsoft Emojis:
   https://emojipedia.org/microsoft/

"""

import os
from pathlib import Path
import sys


def get_icon() -> str:
    """Get the path to the icon file.

    The icon path depends on the mode of the application.

    If it is executed as a compiled ".exe" the is_bundled will
    return true and the icon file must be located in the resources directory.
    Else the icon must be located in the static directory.

    Returns:
        The icon path.

    """

    icon_name: str = "icon.png"
    icon_file: str = ""

    if is_bundled():
        icon_file = os.path.join(os.path.join(os.getcwd(), "resources/"), icon_name)
    else:
        file = os.path.dirname(__file__)
        icon_file = os.path.join(Path(file).parent.absolute(), "static", icon_name)

    return icon_file


def is_bundled() -> bool:
    """Check if the app is running in bundled mode

    Returns:
        True if the app starts bundled (for example a pyinstaller exe).
        False otherwise.

    """

    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return True

    return False
