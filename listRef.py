import json
import sys
from operator import truediv
from os import listdir, walk
from os.path import isfile, join, relpath, abspath
from bs4 import BeautifulSoup
from checkFile import checkFileHasRef
from env import *

def listRef(targetPath) :
    rootReltargetPath=relpath(targetPath, rootFolder)
    fileList=[]

    for (directory, subDirectory, files) in walk(rootFolder):
        for fileName in files:
            if checkFileHasRef(directory,fileName,targetPath,rootReltargetPath):
                fileList.append({'path': directory+'/'+fileName})

    return fileList
    # sys.stdout.flush()
    # json_files = json.dumps(fileList,indent=4)
    # with open('./listRefFile.json','w') as outputFile:
    #     outputFile.write(json_files)
    # outputFile.close()

    # attrList = list(set(attrList)) 
    # for attr in attrList :
    #     print(attr)


# with open('/home/elisee/Bureau/code/eturnity_expert/analysis/deadcode.json') as my_file:
#     data = json.load(my_file)

# for pathFile in data['unusedFiles']:
#     os.remove(pathFile)
