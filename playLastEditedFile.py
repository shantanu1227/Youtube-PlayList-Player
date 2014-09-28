#!/usr/bin/python

import os
import subprocess
import sys

currentDir = os.path.dirname(os.path.realpath(__file__))

lastFile = subprocess.check_output('cd '+currentDir+' && ls -t |head -1', shell=True)
#Removing the \n from the last
lastFile = os.getcwd()+"/"+lastFile[:-1]

#Play The song using mplayer
os.system('mplayer "' +lastFile+'"')

if len(sys.argv) == 0:
	os.system('rm "'+lastFile+'"')
elif str(sys.argv).find("save") < 0:
	os.system('rm "'+lastFile+'"')
exit()
#https://www.youtube.com/watch?list=RDmWRsgZuwf_8