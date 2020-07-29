class UrlQuery:
    def __init__(self):
        pass

    def query(self, target):
        if target == "apod":
            self._query_apod()
        elif target == "bing":
            self._query_bing()
        else:
            raise ValueError(target)

    def _query_apod(self):
        pass

    def _query_bing(self):
        pass
