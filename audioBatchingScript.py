import os, shutil
from mutagen.wave import WAVE
mainDirectory = r"/home/ubuntu/fileBatchTest/test/"
os.chdir(mainDirectory)
obj = os.scandir()

# def convert(seconds):
#     hours = seconds // 3600
#     seconds %= 3600
#     mins = seconds // 60
#     seconds %= 60
#     return(hours, mins, seconds)

totalLength = 0
i = 1
newDirectory = mainDirectory + str(i) + "/"

os.mkdir(newDirectory)

for entry in obj:
    if entry.is_file():
        audio = WAVE(entry)
        length = int(audio.info.length)
        print("this file is " + str(length) + " seconds")
        totalLength = totalLength + length
        print ("running total is " + str(totalLength) + " seconds")
        if totalLength <= 3600 and length < 600 :
            shutil.move(mainDirectory + str(entry.name), str(newDirectory + entry.name))
            print(entry.name + " has been moved: " + str(totalLength) + " seconds have been used")
        else:
            i = i+1
            newDirectory = mainDirectory + str(i) + "/"
            os.mkdir(newDirectory)
            shutil.move(mainDirectory + str(entry.name), str(newDirectory + entry.name))
            print(newDirectory + " has been created")
            totalLength = 0
            print("Running total is reset: " + str(totalLength))
obj.close()