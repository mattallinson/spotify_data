# Spotify Data Wrangling
Tools for turning a Spotify data dump into charts, tables and graphs.

## Introduction
Spotify data is for life, not just for Christmas. Spotify's app lets you play with a year's worth of data every December, but you can actually request all your data be sent to you. Information on how to do this can be found on [Spotify's website here](https://www.spotify.com/us/account/privacy/). Be prepared to wait a long time to get sent the data.

The data is sent to you as a zip file that contains JSON files. If, like me, you've had Spotify for a long time, it's a lot of files. This repo will contain tools and resources for exploring this data. But for now it contains one tool only, which is for turning the zip of JSON files into an excel spreadsheet.

## Requirements
This repository required [Pandas](https://pandas.pydata.org/docs/getting_started/install.html) to run. Your best bet for this is to [install Anaconda](https://docs.continuum.io/anaconda/install/). You can try with pip, but you're on your own I'm afraid.

An optional extra module is [`titlecase`](https://pypi.org/project/titlecase/) which can be installed via 
```
$> pip install titlecase
```
There's more information on song names below

## Usage
Make a folder with `spotify_tools.py` and `my_spotify_data.zip` in it together, open a terminal window at the folder you've just made and then run
```
$> python spotify_tools.py
```  
If it runs correctly, it will create 3 folders (Pickle, JSON and Excel) and your freshly combined data will be saved in `/Excel/streams.xlsx`

## Song Names
Over time, Spotify's records of some song names have changed. For example small words (e.g. 'of') go from being uncapitalised to capitalised and back again, or song titles by *SOPHIE* changed from being Title Case to all caps.  This created quite serious issues for counting songs and ranking them by number of plays (especially for *SOPHIE* fans, like myself.) I thought about a code that found all songs with the same URI but different titles, and then standardising them to the latest version, however that method would be *very* time consuing for not a lot of benefit. Changing all song titles to ALL CAPS or no caps also looked stupid, and Title Case has the bad habit of making `you're` correct to `You'Re` which looks ***exceedingly*** stupid. In the end I've gone for the third party library titlecase which handles things nicely if a little slowly, and if it's not installed it runs anyway with the in-build TitleCase option instead. I appreciate that the naming of a piece of art is part of the art, and the capitalisation of the name is part of the name, and it's problematic to change the name on a piece of work (e.g. rendering *SOPHIE's BIPP* as *Bipp*) when it's not your work, but ultimately it's only a minor change and a major help so I feel empowered to make it. 
