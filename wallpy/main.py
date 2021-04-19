import os

import click

from screeninfo import get_monitors

from wallpy.__version__ import VERSION
from wallpy.gui.main_window import MainWindow
from wallpy.gui.icon import get_icon

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option(
    "--apod",
    "-a",
    "apod",
    is_flag=True,
    help="Download the Astronomy Picture of the Day (APoD)",
)
@click.option(
    "--bing",
    "-b",
    "bing",
    is_flag=True,
    help="Download the Bing image of the Day (BIoD)",
)
@click.option("--script", "-s", "script", is_flag=True)
@click.option("--file", "-f", "file", help="Use the file as wallpaper")
@click.option("--gui", "-g", "gui", is_flag=True)
def main(apod, bing, file, gui, script):
    click.echo(f"Welcome to wallpy! v{VERSION}")

    monitors = get_monitors()
    print(f"Found {len(monitors)} monitor(s)")

    if gui is not None:
        app = MainWindow("Wallpy", "at.martinmoser.wallpy", icon=get_icon())
        app.main_loop()

    # if file is None:
    #     fp = tempfile.TemporaryDirectory()
    #     file = os.path.join(fp.name, "wallpaper.jpg")
    #     url = ""
    #
    #     if apod:
    #         url = UrlQuery().query("apod")
    #
    #     elif bing:
    #         url = UrlQuery().query("bing")
    #
    #     try:
    #         ImageDownload().download(url, file)
    #     except URLError:
    #         click.echo("Could not download the image! The url was invalid")
    #         sys.exit(1)
    #
    #
    # set_wallpaper(file)
    #
    # # sleep for a short time
    # # required to properly set the background
    # # TODO:
    # #      * Maybe this changes when this is not the end of the code
    # time.sleep(0.5)
    #
    # if script:
    #     msg: str = ""
    #
    #     if apod:
    #         msg = "Set the new APOD from NASA as wallpaper"
    #     elif bing:
    #         msg = "Set the new Image of the day from Bing as wallpaper"
    #
    #     notificate(title="Wallpy", text=msg)


if __name__ == "__main__":
    main()
