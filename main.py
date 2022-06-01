from email import header
from platform import architecture
from re import A
import streamlit as st
import random as rd
import pandas as pd


#--------------------------------------------------------------------------------

def loadData(path):
    '''
    loads data from a pkl file
    '''
    return pd.read_pickle(path)

def listTracksNamesAndArtistsInPlaylist(df, pid):
    '''
    returns a list of tracks names and artists in a playlist
    '''

    return df[df['pid']==pid]['track_name'].tolist()

n = 5

def randomNumGenerator(n):
    '''
    returns n random numbers
    '''
    return (rd.randint(0, 500) for i in range(n))


def listPlaylistNames(df, pid_list):
    '''
    returns a list of playlist names
    '''
    playlist_name = tuple([df[df['pid']==pid]['playlist_name'].tolist()[0] for pid in pid_list])
    return playlist_name

def getPlaylistNumber(df, p_name):
    '''
    returns the playlist number of a playlist name
    '''
    return df[df['playlist_name']==p_name]['pid'].tolist()[0]

if __name__ == '__main__':
    df = loadData('data/tracks_playlist_500.pkl')
    res = loadData('data/res.pkl')
    pid_list = randomNumGenerator(n)
    markdown1 ='''

    A collaborative filtering technique to recommend tracks to a playlist based on similair playlist/s. \n 
    Visit this [link](https://shreyasprasad.com/paper/2022/06/01/Spotify-Recommendations-Using-Embarrassingly-Shallow-Autoencoders-for-Sparse-Data.html) for more info
    '''


# -----------------------    Interface              ---------------------------------------------------------

header = st.container()
c1 = st.container()
c2 = st.container()
c3 = st.container()

with header:
    st.title("Spotify Recommender for Playlists")
    st.markdown(markdown1)

with c1:
    st.header("Select Playlist")
    option = st.selectbox( 'List of Randomly generated playlists', listPlaylistNames(df, pid_list))
    pid = getPlaylistNumber(df, option)


with c2:
    st.header("Songs in the Playlist: " + option)
    st.write(listTracksNamesAndArtistsInPlaylist(df, pid))


with c3:
    st.header("Recommendation for the Playlist: " + option)
    st.write(listTracksNamesAndArtistsInPlaylist(res, pid))
