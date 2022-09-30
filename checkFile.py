
from os.path import relpath, splitext
def checkFileHasRef(directory,fileName,targetPath,rootReltargetPath):
    if fileName.endswith(".vue"):
        with open(directory+"/"+fileName) as f:
            relTargetPath = relpath(targetPath, directory)
            relTargetPath = splitext(relTargetPath)[0]
            rootReltargetPath=splitext(rootReltargetPath)[0]

            fcontent=f.read()       
            if relTargetPath in fcontent or rootReltargetPath in fcontent:
                return True
            else : 
                return False
    else :
        return False

def isVue(directory,fileName):
    return fileName.endswith(".vue")

def hasSharedInputNumber(directory,fileName):
    if fileName.endswith(".vue"):
        with open(directory+"/"+fileName) as f:
            fcontent=f.read()
            needle="nents/shared/InputNumber"   
            if needle in fcontent:
                print(directory+"/"+fileName)
                return True
            else : 
                return False
    else :
        return False




