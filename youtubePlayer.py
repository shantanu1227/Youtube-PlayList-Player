#!/usr/bin/python

import os
current_dir = os.path.dirname(os.path.realpath(__file__))
youtubePlayListLink = 'https://www.youtube.com/watch?list='+raw_input("Enter the Playlist Link Id: ");
anyOtherCommand = "--playlist-start "+raw_input("Start PlayList Index: ")
playerFile = current_dir+"/playLastEditedFile.py"
os.system('cd '+current_dir+' && youtube-dl --restrict-filenames '+anyOtherCommand+'  --no-mtime -w --no-part --extract-audio -i --audio-format mp3 --exec "'+playerFile+'" ' +youtubePlayListLink)

#https://www.youtube.com/watch?list=RDmWRsgZuwf_8
