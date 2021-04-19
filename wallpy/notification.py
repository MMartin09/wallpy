import clr

clr.AddReference("System.Windows.Forms")

import System.Windows.Forms as WinForms  # noqa: F401, E402
from System.Drawing import SystemIcons  # noqa: F401


def notificate(title, text, type="exclamation") -> None:
    """Show a notification message.

    Currently only "exclamation" type is supported.

    Args:
        title (str): Title of the notification
        text (str): Text of the notification
        type (str): Type of the notification (Used for the notification icon)

    """

    toast = WinForms.NotifyIcon()

    if type == "exclamation":
        toast.Icon = SystemIcons.Exclamation
    else:
        raise ValueError(type)

    toast.BalloonTipTitle = title
    toast.BalloonTipText = text

    toast.Visible = True
    toast.ShowBalloonTip(3000)
