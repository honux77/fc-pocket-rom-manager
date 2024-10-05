'''
파일 관련 유틸리티 함수들
'''

import os
from os import path
import re
import tkinter as tk
from tkinter import messagebox as mBox

from config import Config
config = Config()

def getExtension(f):
    '''
    파일의 확장자를 반환한다.
    '''
    return path.splitext(f)[1]

def changeRootDir():
    os.chdir(config.getBasePath())

def changeSubRomDir(subPath):
    os.chdir(path.join(config.getBasePath(), subPath))

def readSubDirs():        
    '''
    roms 폴더의 하위 폴더를 읽어서 정렬된 리스트로 반환한다.
    바이오스 폴더는 제외한다.    
    '''
    romDir = [f for f in os.listdir() if path.isdir(f) and f != 'bios']
    romDir.sort()
    return romDir

def findSimilarImage(romDir, romName, imgDir):
    
    '''
    romName과 가장 유사한 이미지 이름을 찾아서 반환한다.
    romDir: roms 폴더의 하위 폴더
    romName: 롬 이름
    imgDir: rom 폴더 하위의 images 폴더
    '''
    
    import fuzzywuzzy.process as fuzzProcess
    allImages = [f for f in os.listdir(path.join(romDir, imgDir)) if path.isfile(path.join(romDir, imgDir, f))]    
    return fuzzProcess.extractOne(romName, allImages)

def imageDelete(imgPath, romPath):
    import os
    from os import path

    roms = [os.path.splitext(f)[0] for f in os.listdir(romPath)]
    imgs = [os.path.splitext(f)[0] for f in os.listdir(imgPath)]

    for f in imgs:
        if f not in roms:
            print("Roms not exists: ", f)
            os.remove(path.join(imgPath, f + '.png'))


def printRomInfo(imgPath, romPath):
    import os
    from os import path

    roms = [os.path.splitext(f)[0] for f in os.listdir(romPath)]
    imgs = [os.path.splitext(f)[0] for f in os.listdir(imgPath)]

    for f in roms:
        if f not in imgs:
            print("Image not exists: ", f)

def deleteRomAndImages(subPath, romPath, imggePath):
    msg = ""
    result = mBox.askquestion("삭제", "{}\n {}\n 선택된 롬과 이미지를 삭제하시겠습니까?".format(romPath, imggePath))

    if result == 'no':
        return "삭제 취소"
    
    rom = path.join(subPath, romPath)    
    img = path.join(subPath, imggePath)
    try:
        os.remove(rom)
    except:
        msg += "롬 삭제 실패"
    try:
        os.remove(img)    
    except:
        msg += "이미지 삭제 실패"
        return msg
    return romPath + " 삭제 성공"

# main function for test
if __name__ == "__main__":
    os.chdir(ROM_PATH)
    print("Test for Similar Image")
    print(findSimilarImage('gb', "Super Mario world", "box"))