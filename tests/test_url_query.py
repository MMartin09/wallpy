import pytest

from wallpy.url_query import UrlQuery


class TestUrlQuery:
    url_query = UrlQuery()

    def test_query_invalid_target(self):
        with pytest.raises(ValueError):
            self.url_query.query("invalid")
