from win10toast import ToastNotifier

import ctypes

import clr

clr.AddReference("System.Windows.Forms")

import System.Windows.Forms as WinForms  # noqa: F401, E402
from System.Drawing import SystemIcons   # noqa: F401

class Notification:

    def __init__(self):
        pass

    def show_notification(self):
        pass


def main():
    notifyIcon1 = WinForms.NotifyIcon()
    notifyIcon1.Icon = SystemIcons.Exclamation
    notifyIcon1.BalloonTipTitle = "Balloon Tip Title"
    notifyIcon1.BalloonTipText = "Balloon Tip Text."
    notifyIcon1.Visible = True
    notifyIcon1.ShowBalloonTip(3000)


if __name__ == '__main__':
    main()
