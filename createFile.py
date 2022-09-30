from os.path import relpath, abspath,dirname

def createFile(content,filePath):
    with open(filePath, "w") as f:
        f.write(content)
        f.close()

