
import ctypes
import random


#******************* Select file name *************************************************************
def getFilesName():
    #Select file name
    import os

    #Open dialog
    filesDir =  'C:\\Users\\dravasio\\Pictures\\Wallpapers\\'

    filePaths = []

    for dirpath, dirnames, files in os.walk(filesDir):
    #print('Found directory: {dirpath}')
        for file_name in files:
            if file_name.endswith(".jpg") or  file_name.endswith(".JPG"):

                print(file_name)
                _PathModifiedTemp = dirpath
                newPath = (_PathModifiedTemp.replace('\\', '/'))
                filePaths.append(newPath + '/' + file_name)

    return filePaths

filePaths = getFilesName()
listLenght = len(filePaths)
randomInteger = random.randint(0,(listLenght-1))
ctypes.windll.user32.SystemParametersInfoW(20, 0, filePaths[randomInteger] , 1)
