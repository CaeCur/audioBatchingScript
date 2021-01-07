import os, shutil
from mutagen.wave import WAVE
os.chdir(r"/home/ubuntu/fileBatchTest/VoipMan01test")
obj = os.scandir() 

totalLength = 0
i = 1
newDirectory = "./" + str(i) + "/"

for entry in obj:
    if entry.is_file():
        audio = WAVE(entry)
        length = int(audio.info.length)
        
obj.close()