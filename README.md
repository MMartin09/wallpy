# Wallpy

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/MMartin09/wallpy?include_prereleases&style=for-the-badge)
[![GitHub license](https://img.shields.io/github/license/MMartin09/wallpy?style=for-the-badge)](https://github.com/MMartin09/wallpy/blob/development/LICENSE)
[![style black](https://img.shields.io/badge/Style-Black-black.svg?style=for-the-badge)](https://github.com/ambv/black)

Wallpy is a simple cli application to change your desktop wallpaper. 
It could automatically pull the Astronomy Picture of the Day (APoD) from NASA or the Bing image of the day and set it as wallpaper. 
You could also set a local image file as wallpaper. 

## Installation

Wallpy is available on PyPi and could be installed with `pip`. 
To install the latest version of wallpy run the command

`pip install wallpy`

To install and upgrad run 

`pip3 install --user --upgrade wallpy`

## Usage

```
Usage: wallpy [OPTIONS]

Options:
  -a, --apod       Download the Astronomy Picture of the Day (APoD)
  -b, --bing       Download the Bing image of the day
  -f, --file TEXT  Use the file as wallpaper
  -h, --help       Show this message and exit.
```

## Contributions

For the code to be merged, each new code must be formatted with [black](https://black.readthedocs.io) for consistency with the rest of the code. 
Before introducing any major features or changes to the core functionality please consider opening [an issue](https://github.com/MMartin09/wallpy/issues) to outline your proposal. 
