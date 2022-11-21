# Spotify Data Wrangling

## Introduction
Spotify data is for life, not just for Christmas. Spotify's app lets you play with a year's worth of data every December, but you can actually request all your data be sent to you. It takes up to a month for them to send it to you. Information on how to do this can be found on [Spotify's website here](https://www.spotify.com/us/account/privacy/).

The data is sent to you as a zip file that contains JSON files. If, like me, you've had Spotify for a long time, it's a lot of files. This repo will contain tools and resources for exploring this data. But for now it contains one tool only, which is for turning the zip of JSON files into an excel spreadsheet. 

## Requirements
This repository required [Pandas](https://pandas.pydata.org/docs/getting_started/install.html) to run. Your best bet for this is to [install Anaconda](https://docs.continuum.io/anaconda/install/). If you only want to use the tool for converting the zip to excel and don't want to install all of Anaconda just to do that, you can try 
```$> pip install pandas```
but you're very much on your own with that I'm afraid. 

## Usage
Make a folder with `spotify_tools.py` and `my_spotify_data.zip` in it together, open a terminal window at the folder you've just made and then run
```
$> python spotify_tools.py
```  
If it runs correctly, it will create 3 folders (Pickle, JSON and Excel) and your freshly combined data will be saved in `/Excel/streams.xlsx`
