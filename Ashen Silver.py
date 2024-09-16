#importing custom libraries
import Constants as c
#importing default libraries
from natsort import natsorted
import os
import time
import pyautogui
import pygetwindow
import subprocess

#program constants, small
keysIn_folderAdressList = list(c.folderAdressList.keys())
hasC = "& Has A Comment"
path_masterFolder = r"D:\Ashen Silver\More\Master"

#program variables
filesInMasterFolder = []

#functions
#functions set 1
def addFilesTo_filesInMasterFolder():
    global filesInMasterFolder
    global path_masterFolder
    for fileName in os.listdir(path_masterFolder):
        if os.path.isfile(os.path.join(path_masterFolder, fileName)):
            filesInMasterFolder.append(fileName)
    filesInMasterFolder = natsorted(filesInMasterFolder)

def getDbSize():
    dbSize = os.path.getsize(r"E:\Code\Laptop Code\Ashen Silver Manager\Database\Log of Commands by the User.csv")
    if dbSize > 50000000:
        print("The past-logs' size is over 50 mb.\n")

#functions set 2
def allWindowsSetup(imageWindow):
    global path_masterFolder
    windowSetup_windowsSnap(r"C:\Users\vinee\AppData\Local\Programs\Python\Launcher\py.exe", "right")
    time.sleep(0.5)
    subprocess.run(['start', '', os.path.join(path_masterFolder, imageWindow)], shell=True)
    time.sleep(0.5)
    windowSetup_windowsSnap(imageWindow, "left")
    windowSetup_windowsSnapReposition()

def windowSetup_windowsSnap(windowName, position):
    windowObject = pygetwindow.getWindowsWithTitle(windowName)
    if windowObject:
        windowObject = windowObject[0]
        windowObject.restore()
        windowObject.activate()
        windowObject.maximize()
        time.sleep(0.5)
        pyautogui.hotkey("win", position)
    else:
        time.sleep(0.25)
        windowSetup_windowsSnap(windowName, position)

def windowSetup_windowsSnapReposition():
    pyautogui.moveTo(960, 509)
    time.sleep(0.5)
    pyautogui.mouseDown()
    pyautogui.moveTo(1600, 509, duration=0.5)
    pyautogui.mouseUp()
    pyautogui.moveTo(1872, 86)
    pyautogui.click()

#functions set 3
def programSafety(value):
    #read
    programSafetyObject = open(r"E:\Code\Laptop Code\Ashen Silver Manager\Database\Safety of the Last App Exit.txt", "rt")
    programSafety_lastValue = int(programSafetyObject.read())
    programSafetyObject.close()
    #write
    programSafetyObject = open(r"E:\Code\Laptop Code\Ashen Silver Manager\Database\Safety of the Last App Exit.txt", "wt")
    programSafetyObject.write(str(value))
    programSafetyObject.close()
    #return
    return programSafety_lastValue

def readUniqueFileID():
    uniqueFileIdObject = open(r"E:\Code\Laptop Code\Ashen Silver Manager\Database\Unique Image ID.txt", "rt")
    uniqueFileId_lastValue = int(uniqueFileIdObject.read())
    uniqueFileIdObject.close()
    return uniqueFileId_lastValue

def writeToUniqueFileID(value):
    uniqueFileIdObject = open(r"E:\Code\Laptop Code\Ashen Silver Manager\Database\Unique Image ID.txt", "wt")
    uniqueFileIdObject.write(str(value))
    uniqueFileIdObject.close()    

def lastProgramSafety_wasOff(ifLastProgramSafety):
    if ifLastProgramSafety==0:
        global uniqueFileID_value
        print(f"{c.TEXT_BOLD_RED}Program Safety was found as Off.{c.TEXT_RESET}")
        uniqueFileID_value+=10000
        writeToUniqueFileID(uniqueFileID_value)

#function set 4
def renameAndMove_aFile(oldFileName):

#main function
if __name__ == "__main__":
    #starting
    os.chdir(path_masterFolder)
    getDbSize()
    addFilesTo_filesInMasterFolder()
    allWindowsSetup(filesInMasterFolder[0])
    ifLastProgramSafety = programSafety(0)
    uniqueFileID_value = readUniqueFileID()
    lastProgramSafety_wasOff(ifLastProgramSafety)

    #main function of the main function
    for fileName in filesInMasterFolder:
        for i in range(20):
            print("")
        print(c.recurring_printStatement)
        renameAndMove_aFile(fileName)
        
    #ending
    programSafety(1)        
    writeToUniqueFileID(uniqueFileID_value)
    input("\nTask finished! Press Enter to exit.")
    pyautogui.moveTo(1314, 22)
    pyautogui.click()

#the end
