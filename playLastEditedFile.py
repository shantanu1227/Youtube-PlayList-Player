#!/usr/bin/python

import os
import subprocess
current_dir = os.path.dirname(os.path.realpath(__file__))
last_file = subprocess.check_output('cd '+current_dir+' && ls -t |head -1', shell=True)
last_file = os.getcwd()+"/"+last_file[:-1]
os.system('mplayer "' +last_file+'"')
os.system('rm "'+last_file+'"')
exit()
#https://www.youtube.com/watch?list=RDmWRsgZuwf_8