from setuptools import setup

from wallpy.__version__ import VERSION

with open("readme.md", "r") as fp:
    LONG_DESCRIPTION = fp.read()

with open("requirements.txt", "r") as fp:
    REQUIREMENTS = fp.read().splitlines()

setup(
    author="Moser Martin",
    author_email="mosermartin09@gmail.com",
    description="A simple wallpaper app",
    entry_points={"console_scripts": ["wallpy=wallpy.main:main"]},
    install_requires=REQUIREMENTS,
    license="MIT",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    name="wallpy",
    packages=["wallpy"],
    python_requires=">=3.6",
    url="https://github.com/MMartin09/wallpy",
    version=VERSION,
)
