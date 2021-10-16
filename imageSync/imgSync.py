#!/usr/bin/env python3

import glob
import subprocess
import argparse

cardDir = '/media/lurbano/K-1 II/DCIM/'
compDir = '/home/lurbano/Pictures/K1-II/'

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", type=str, default="jpg", help = "file type (case sensitive): 'jpg' or 'raw'")

args = parser.parse_args()

#check file type on SD card
sampleDir = glob.glob(f'{cardDir}*', recursive=True)[0]
sampleFile = glob.glob(f'{sampleDir}/*')[0]
print(sampleFile[-3:])

fType = sampleFile[-3:] # get the extension of the file

cardDir = cardDir.replace(" ", "\ ")
print(cardDir)

if fType == "DNG": #raw
    print("rSyncing raw files (DNG)...")
    subprocess.run(f'rsync -av {cardDir} {compDir}raw', shell=True)
elif fType == "JPG":
    print("rSyncing JPG files")
    subprocess.run(f'rsync -av {cardDir} {compDir}jpg', shell=True)
else:
    print("Could not identify file type.")


#print(args.type)

# if args.type == "jpg":
#     subprocess.run(f'rsync -av /media/lurbano/K-1\ II/DCIM/ /home/lurbano/Pictures/K1-II/jpg', shell=True)
# elif args.type == "raw":
#     subprocess.run(f'rsync -av /media/lurbano/K-1\ II/DCIM/ /home/lurbano/Pictures/K1-II/raw', shell=True)
# else:
#     print('File type should be either "jpg" or "raw"')
