# Spotify Data Wrangling
Tools for turning a Spotify data dump into charts, tables and graphs.

## Introduction
Spotify data is for life, not just for Christmas. Spotify's app lets you play with a year's worth of data every December, but you can actually request all your data be sent to you. Information on how to do this can be found on [Spotify's website here](https://www.spotify.com/us/account/privacy/). Be prepared to wait a long time to get sent the data.

The data is sent to you as a zip file that contains JSON files. If, like me, you've had Spotify for a long time, it's a lot of files. This repo will contain tools and resources for exploring this data. But for now it contains one tool only, which is for turning the zip of JSON files into an excel spreadsheet.

## Requirements
This repository required [Pandas](https://pandas.pydata.org/docs/getting_started/install.html) to run. Your best bet for this is to [install Anaconda](https://docs.continuum.io/anaconda/install/). You can try with pip, but you're on your own I'm afraid.

## Usage
Make a folder with `spotify_tools.py` and `my_spotify_data.zip` in it together, open a terminal window at the folder you've just made and then run
```
$> python spotify_tools.py
```  
If it runs correctly, it will create 3 folders (Pickle, JSON and Excel) and your freshly combined data will be saved in `/Excel/streams.xlsx`
