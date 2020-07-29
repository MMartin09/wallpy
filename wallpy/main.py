import tempfile
import os
import time

import click

from wallpy.wallpaper import set_wallpaper
from wallpy.apod_downloader import download_apod, download_bing

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option("--apod", "-a", show_default=True, is_flag=True)
@click.option("--bing", "-b", show_default=True, is_flag=True)
def main(apod, bing):
    click.echo("Welcome to wallpy!")

    # apod = True
    bing = True

    if apod:
        fp = tempfile.TemporaryDirectory()
        download_apod(os.path.join(fp.name, "test.jpg"))
        set_wallpaper(os.path.join(fp.name, "test.jpg"))

        # sleep for a short time
        # required to properly set the background
        # TODO:
        #      * Maybe this changes when this is not the end of the code
        time.sleep(0.5)

    elif bing:
        fp = tempfile.TemporaryDirectory()
        download_bing(os.path.join(fp.name, "test.jpg"))
        set_wallpaper(os.path.join(fp.name, "test.jpg"))

        # sleep for a short time
        # required to properly set the background
        # TODO:
        #      * Maybe this changes when this is not the end of the code
        time.sleep(0.5)


if __name__ == "__main__":
    main()
