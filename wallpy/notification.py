import clr

clr.AddReference("System.Windows.Forms")

import System.Windows.Forms as WinForms  # noqa: F401, E402
from System.Drawing import SystemIcons   # noqa: F401


class Notification:

    _toast = WinForms.NotifyIcon

    def __init__(self, title, text, type = "exclamation"):
        self._toast = WinForms.NotifyIcon()

        if type == "exclamation":
            self._toast.Icon = SystemIcons.Exclamation
        else:
            raise ValueError(type)

        self._toast.BallonTipTitle = title
        self._toast.BalloonTipText = text

    def show_notification(self):
        self._toast.Visible = True
        self._toast.ShowBalloonTip(3000)


def main():
    Notification("Wally", "Downloaded the new image of the day from Bing").show_notification()


if __name__ == '__main__':
    main()
