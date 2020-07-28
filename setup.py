from setuptools import setup

from wallpy.__version__ import VERSION

with open("readme.md", "r") as fp:
    LONG_DESCRIPTION = fp.read()

setup(
    author="Moser Martin",
    author_email="mosermartin09@gmail.com",
    description="Python wallpaper",
    license="MIT",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    name="wallpy",
    packages=["wallpy"],
    url="https://github.com/MMartin09/wallpy",
    version=VERSION,
)
