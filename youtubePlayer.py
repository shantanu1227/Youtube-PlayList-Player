#!/usr/bin/python

import subprocess
import os


def emptyLastLine():
	CURSOR_UP_ONE = '\x1b[1A'
	ERASE_LINE = '\x1b[2K'
	print(CURSOR_UP_ONE + ERASE_LINE)

DEVNULL = open(os.devnull, 'wb')
current_dir = os.path.dirname(os.path.realpath(__file__))
saveFile = 0
playlistStartIndex = 1

#playerFile - Plays the last modified file
playerFile = current_dir+"/playLastEditedFile.py"

youtubePlayListLink = 'https://www.youtube.com/watch?list='+raw_input("Enter the Playlist Link Id: ");

try:
  playlistStartIndex = int(raw_input("Start PlayList Index: "))
except ValueError:
  playlistStartIndex = 1

playlistStartIndex = "--playlist-start " + str(playlistStartIndex)

try:
  saveFile = int(raw_input("Do you want to save the Files (1/0) :" ))
except ValueError:
  saveFile = 0

if saveFile==1:
  #playerFile - Plays the last modified file
  playerFile = current_dir+"/playLastEditedFile.py save"

youtubeDlCommand = 'youtube-dl --restrict-filenames '+playlistStartIndex+' --no-warnings --no-mtime -w --no-part --extract-audio -i --audio-format mp3 --exec "'+playerFile+'" ' +youtubePlayListLink

proc = subprocess.Popen(['cd '+current_dir+' && '+youtubeDlCommand],stdout=subprocess.PIPE,stderr=DEVNULL,shell=True)

while True:
  line = proc.stdout.readline()
  if line != '':
    if line.find("exec") > 0:
      fileName = line.rstrip().split(":")
      print "Playing Song: ", fileName[1].strip().split()[-1]
  else:
    break
#https://www.youtube.com/watch?list=RDmWRsgZuwf_8
