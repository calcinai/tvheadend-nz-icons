# New Zealand TV and radio logos for TVheadend

## Introduction

This repository contains icons for New Zealand satellite (Freeview and Sky) and terrestrial (Freeview) television channel and radio stations for use with [TVheadend](https://tvheadend.org).

The submodule is [Jasmeet181/mediaportal-nz-logos](https://github.com/Jasmeet181/mediaportal-nz-logos) and there's a simple generator script to parse that repository and generate a folder of symlinks named by service identifier.


## Usage

Clone this repository somewhere on the TVheadend server (it's a good idea to add `--depth=1` due to the images changing)

    git clone git@github.com:calcinai/tvheadend-nz-icons.git --recurse-submodules --shallow-submodules --depth=1
    
Configure TVheadend to look in the icons directoy for the symlinks by setting the channel icon path to something like `file:///home/hts/tvheadend-nz-icons/icons/%c`


### Acknowledgments

Thanks to [Jasmeet181](https://github.com/Jasmeet181) for all the work on the source images and data!