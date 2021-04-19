# Wallpy

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/MMartin09/wallpy?include_prereleases)
[![GitHub license](https://img.shields.io/github/license/MMartin09/wallpy)](https://github.com/MMartin09/wallpy/blob/development/LICENSE)
[![style black](https://img.shields.io/badge/Style-Black-black.svg)](https://github.com/ambv/black)

Wallpy is a simple cli application to change your desktop wallpaper. 
It could automatically pull the Astronomy Picture of the Day (APoD) from NASA or the Bing image of the day (BIoD) and set it as wallpaper. 
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

## Executable

Wallpy could also be used without installation. The `bin` directory contains the pre-compiled `.exe` file. 
It requires no installation and no Python. The usage is the same as described in the section 'Usage'. 
The only difference is, that the application must be called with `wallpy.exe`. 

The `bin`folder contains two batch files. `wallpy-apod` sets the APoD and `wallpy-bing` the bing image. 
They could by executed with a double click on it. 

## Contributions

For the code to be merged, each new code must be formatted with [black](https://black.readthedocs.io) for consistency with the rest of the code. 
Before introducing any major features or changes to the core functionality please consider opening [an issue](https://github.com/MMartin09/wallpy/issues) to outline your proposal. 

