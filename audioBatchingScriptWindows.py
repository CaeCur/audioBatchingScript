import os, shutil
from mutagen.wave import WAVE
os.chdir(r"C:\Users\Caelan\Desktop\Constellation")
obj = os.scandir()
 
# def convert(seconds):
#     hours = seconds // 3600
#     seconds %= 3600
#     mins = seconds // 60
#     seconds %= 60
#     return(hours, mins, seconds)

totalLength = 0
i = 1
newDirectory = "./" + str(i)

if totalLength <= 3600:
    os.mkdir(newDirectory)

for entry in obj:
    if entry.is_dir() or entry.is_file():
        audio = WAVE(entry)
        length = int(audio.info.length)
        totalLength = totalLength + length
        if totalLength <= 3600:
            shutil.move(entry, newDirectory)
        else:
            i = i+1
            newDirectory = "./" + str(i)
            os.mkdir(newDirectory)
            shutil.move(entry, newDirectory)
            totalLength = 0
obj.close()