from operator import truediv
from os import listdir, walk
from os.path import isfile, join, relpath, abspath
from checkFile import isVue
from env import *

def listFile():
    fileList=[]
    for (directory, subDirectory, files) in walk(rootFolder):
        for fileName in files:
            if isVue(directory,fileName):
                fileList.append({"path": directory+"/"+fileName})
    return fileList
  
