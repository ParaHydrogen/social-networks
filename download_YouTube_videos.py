"""
Little program that can be used to download YouTube videos or playlist.
This could probably be optimized but it works more than well as it is.
"""

import os
from pytube import *

path_to_download_files = r"D:\YT audio\Electronic Gems"
os.chdir(path_to_download_files)

# link_video = 'https://www.youtube.com/watch?v=mRJSIYmHuNI'
# link_playlist = "https://www.youtube.com/playlist?list=PL63ZO-jXFTasqvj7WdEFQ6QtG6UBrl9CR"


def doesResolutionExists(link_video, resolution):

    link_video = str(link_video)
    resolution = str(resolution)

    yt = YouTube(link_video)

    stream_resolution = yt.streams.filter(res=resolution, progressive=True)
    if stream_resolution is not None:
        return True
    else:
        return False


def downloadVideo(link_video, resolution, *option):
    yt = YouTube(link_video)
    if option == 'audio':
        yt.streams.get_audio_only().download()
        print('The audio: ' + link_video + ' succesfully downloaded')
    else:
        if doesResolutionExists(link_video, resolution) is True:
            try:
                yt.streams.get_by_resolution(resolution).download()
                print('The video: ' + link_video + ' succesfully downloaded')
            except:
                print('The resolution: ' + resolution + ' is not available')


# -- Download a playlist


def downloadPlaylist(link_playlist):

    list_links_playlist = list(Playlist(link_playlist))
    downloaded_videos = []
    # print(list_links_playlist)

    c = len(list_links_playlist)
    i = 0

    while i < c:
        try:
            print(str(i + 1) + '/' + str(c))
            link_video = list_links_playlist[i]
            downloadVideo(link_video, '360p', 'audio')
            i += 1
        except:
            i += 1
            continue


# downloadPlaylist(link_playlist)
