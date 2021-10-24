#!/usr/bin/env python3

import glob
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dir", type=str, help = "input directory (terminate with / )")
parser.add_argument("-t", "--type", type=str, default="JPG", help = "file type extension (case sensitive) (default='JPG')")

args = parser.parse_args()

dir = f'{args.dir}*.{args.type}'
dir = dir.replace("\\", "")

print("dir: ", dir)
print("type: ", args.type)



files = glob.glob(dir)

#print(files)
n = 0
for f in files:
    n += 1
    f = f.replace(" ", "\ ")
    print(f)
    outName = f.split("/")[-2] + "_" + f.split("/")[-1]
    outName = outName.replace(args.type, "png")
    print(outName)
    print(f'({n}/{len(files)})')
    subprocess.run(f'convert {f} -resize 2000x2000 {outName}', shell=True)
