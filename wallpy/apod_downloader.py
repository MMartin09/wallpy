import requests
import wget

from wallpy.types import FILE_TYPE


def download_apod(out_file) -> None:
    """Download the APOD from NASA.

    Args:
        out_file (str): The output file where the image should be written.

    """

    apod = query_apod()

    if not apod_filetype(apod) is FILE_TYPE.IMAGE:
        raise TypeError("Error: APOD is no image!")

    wget.download(apod["url"], out=out_file)


def query_apod() -> dict:
    """Query the APOD.

    Returns:
        The query result.

    """

    r = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")

    return r.json()


def apod_filetype(apod) -> FILE_TYPE:
    if apod["media_type"] == "image":
        return FILE_TYPE.IMAGE
    else:
        return FILE_TYPE.VIDEO
