import tempfile
import os

import click

from wallpy.wallpaper import set_wallpaper
from wallpy.apod_downloader import download_apod

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option("--apod", "-a", show_default=True, is_flag=True)
def main(apod):

    apod = True

    if apod:
        fp = tempfile.TemporaryDirectory()
        download_apod(os.path.join(fp.name, "test.jpg"))
        print(os.path.join(fp.name, "test.jpg"))
        set_wallpaper(os.path.join(fp.name, "test.jpg"))

    click.echo("Welcome to wallpy!")

    while True:
        x = 1


if __name__ == "__main__":
    main()
