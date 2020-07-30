import requests

from wallpy.file_types import FILE_TYPE


class UrlQuery:
    def __init__(self):
        pass

    def query(self, target):
        if target == "apod":
            return self._query_apod()
        elif target == "bing":
            return self._query_bing()
        else:
            raise ValueError(target)

    def _query_apod(self):
        r = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
        respond = r.json()

        if not self._apod_filetype(respond) is FILE_TYPE.IMAGE:
            raise TypeError("Error: APOD is no image!")

        return respond["url"]

    def _query_bing(self):
        r = requests.get(
            "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"
        )

        respond = r.json()

        url = "https://www.bing.com/" + r.json()["images"][0]["url"]
        return url

    def _apod_filetype(self, respond):
        if respond["media_type"] == "image":
            return FILE_TYPE.IMAGE
        else:
            return FILE_TYPE.VIDEO
