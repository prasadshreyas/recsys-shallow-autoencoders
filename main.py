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

def main():
    st.title("Song Recommender for Playlists")
    st.markdown(
        """
        The model has been trained on the Million Playlist Dataset (MPD) which contains 1,000,000 playlists from Spotify.
        We use EASE (Embarrassingly Shallow Autoencoders) developed by Harald Steck to recommend songs to a playlist. Link to the paper [here.](https://dl.acm.org/doi/pdf/10.1145/3308558.3313710?casa_token=1cGSrp9S7HAAAAAA:dBC4UCzkQyILJlH46hZVWqGbDeEMpTm44JnllDY5XC3Kis_D6H4KVA1DCQ38OzKTmwC7O04btPpxQOE)
        """
    )


    # Playlist selection column
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            #### Select a playlist from the dropdown menu to see the recommended songs for that playlist.
            """
        )
        pid_list = randomNumGenerator(n)
        playlist_options = listPlaylistNames(df, pid_list)
        option = st.selectbox('List of Randomly Generated Playlists', playlist_options, key="playlist_selector")
        pid = getPlaylistNumber(df, option)

        # Displaying songs in an interactive format
        with st.expander("See Songs in the Playlist"):
            for song in listTracksNamesAndArtistsInPlaylist(df, pid):
                st.text(song)

    # Recommendation column
    with col2:

        st.markdown(
            """
            #### See the recommended songs for the playlist selected on the left.
            """
        )
        recommended_songs = listTracksNamesAndArtistsInPlaylist(res, pid)
        for song in recommended_songs:
            st.text(song)



if __name__ == '__main__':
    df = loadData('data/tracks_playlist_500.pkl')
    res = loadData('data/res.pkl')
    markdown1 ='''
    A collaborative filtering technique to recommend tracks to a playlist based on similair playlist/s.'''
    main()