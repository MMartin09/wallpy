import click

# from wallpy.wallpaper import set_wallpaper
from wallpy.apod_downloader import download_apod

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option("--apod", "-a", show_default=True, is_flag=True)
def main(apod):

    if apod:
        download_apod("test.jpg")

    click.echo("Welcome to wallpy!")


if __name__ == "__main__":
    main()
