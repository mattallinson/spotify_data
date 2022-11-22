'''Tools for taking a big pile of JSON files in a zip archive and turning
them into something useful for either jupyter books or excel spreadsheets
'''
import os
import string
import json
import zipfile
import pandas as pd
from datetime import datetime
try:                                    # can still run without non-standard library
    from titlecase import titlecase
    use_tc=True 
except ModuleNotFoundError:
    use_tc=False
    
def folder_checker(path):
    # Makes folders for specific data types
    if not os.path.exists(path):
        os.mkdir(path)

def extract_zip_data(zip_file_path, save_pickle=True, save_excel=False,
                     save_json=False, clean_track_names=True):
    '''Gets all the files from the zip and imports them to 
    a combined data frame and saves a pickle for quicker
    future loading, can export this as a combined JSON file
    and/or an Excel file too if required 
    '''
    # extracts data from Zip
    print('Looking for files...')
    combined_data = []
    with zipfile.ZipFile(zip_file_path, mode='r') as archive:
        count=0
        for file in archive.infolist():             
            if 'endsong' in file.filename:                
                count+=1
                combined_data+=json.loads(archive.read(file).decode())
    print('Found', count, 'files')
    
    # makes DataFrame
    print('Making DataFrame...')
    df = pd.DataFrame(combined_data)
    
    # renames the most useful columns something more memorable
    df = df.rename(
        columns = {
            'master_metadata_track_name':'track',
            'master_metadata_album_artist_name':'artist',
            'master_metadata_album_album_name':'album'
        }).sort_values('ts')
    
    # Makes the datetime information more usable
    df['ts']=pd.to_datetime(df['ts'])
    
    # Cleans up track title name to Title Case
    if clean_track_names: 
        if use_tc:
            df.track = [
            titlecase(t) if t is not None else None for t in df.track
            ]
        else:
            df.track = df.track.str.title()
    
    # Make a 'Song' column for graph representation/ easy searching
    df['song']=df['artist']+ ' – ' + df['track']
    
    print('...DataFrame complete')
    
    name='streams'
    # OPTIONAL: saves Excel using Pandas in-built function
    if save_excel:
        _save_excel(df,name)
        
    # OPTIONAL: Saves combined JSON of all song data
    if save_json:
        _save_json(df,name)
    
    # OPTIONAL: Saves a pickle for quick loading
    if save_pickle:
        _save_pickle(df,name)
    
    return df

def make_song_frame(df, song_list, save_pickle=True, save_excel=False,):
    '''Takes a dataFrame of all streams and returns one indexed by individual 
    songs with the values for timestamps, first_played, last_played, number of streams,
    album, track, and artist
    '''

    now = datetime.now().strftime('%H:%M')        
    print(now, 'Compiling song data. Progress updates every minute.\n\tPatience is a virtue...')
    
    data={
        'artist': [],
        'track' : [],
        'album' : [],
        'number_of_streams' : [],
        'number_of_20s_streams' : [],
        'timestamps' : [],
    }
    
    count=0
    for song in song_list:
        if now!=datetime.now().strftime('%H:%M'):
            now = datetime.now().strftime('%H:%M')
            print(now,
                  int(100*(count/len(song_list))),
                  '% of the way through')
        
        count+=1        
        sd = df.loc[df.song==song]
        smd= sd.iloc[0]
        data['artist'].append(smd.artist)
        data['track'].append(smd.track)
        data['album'].append(sd.album.unique())
        data['number_of_streams'].append(len(sd))
        data['number_of_20s_streams'].append(len(
                 sd.loc[sd.ms_played>20000]))
        data['timestamps'].append(sd.ts)
    
    print('...done!')              
    song_data_frame = pd.DataFrame(data=data, index=song_list)
    _save_pickle(song_data_frame,'songs')
                  
    return song_data_frame


def _save_pickle(df, name):
    folder_checker('pickle')
    print('Saving pickle...')
    filename = os.path.join('pickle', name + '.pkl')
    df.to_pickle(filename) 
    print('...Pickle Saved')
    return None


def _save_excel(df, name):
    folder_checker('excel')
    print('Saving Excel...\n...Patience is a virtue...')
    
    filename = os.path.join('excel', name + '.xlsx') 
    
    # makes a dataframe without timezone data as this crashes excel
    edf = df.copy(deep=True)
    edf['ts'] = edf['ts'].dt.tz_localize(None)
        
    # Saves it
    with pd.ExcelWriter(filename) as writer:
        edf.to_excel(writer,index=False)                                    
    print('...Excel saved')
        
    return None


def _save_json(df,name):
    folder_checker('json')
    print('Saving JSON...')
    filename = os.path.join('json', name + '.json')
        
    with open(filename,'w') as outfile:
        df.to_json(
            path_or_buf=outfile,
            orient="split",
            index=False,
            indent=4,
            date_format='iso',
            date_unit='s'
        )
    print('...JSON saved')
    
    return None

def main():
    '''If the file is run in the command line, turns the zip
    file into an excel file and does not save a pickle
    '''
    path = 'my_spotify_data.zip'
    print("Looking for", path, "to turn into an excel file")
    
    if path in os.listdir():
        extract_zip_data(path, save_pickle=False, save_excel=True)
    else:
        print(path,
            'not found, please make sure this script runs in the same folder')


if __name__ == "__main__":
    main()
    