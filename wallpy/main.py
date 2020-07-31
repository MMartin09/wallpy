import tempfile
import os
import time

import click

from wallpy.url_query import UrlQuery
from wallpy.image_download import ImageDownload
from wallpy.wallpaper import set_wallpaper

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
    "--bing", "-b", "bing", is_flag=True, help="Download the Bing image of the day"
)
@click.option("--file", "-f", "file", help="Use the file as wallpaper")
def main(apod, bing, file):
    click.echo("Welcome to wallpy!")

    if file is None:
        fp = tempfile.TemporaryDirectory()
        file = os.path.join(fp.name, "wallpaper.jpg")

        if apod:
            url = UrlQuery().query("apod")
            ImageDownload().download(url, file)

        elif bing:
            url = UrlQuery().query("bing")
            ImageDownload().download(url, file)

    set_wallpaper(file)

    # sleep for a short time
    # required to properly set the background
    # TODO:
    #      * Maybe this changes when this is not the end of the code
    time.sleep(0.5)


if __name__ == "__main__":
    main()
