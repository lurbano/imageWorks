#!/usr/bin/env python3

# Go into directory with image files and program creates a parallel folder in ../small-jpg
#  with the small files

import glob
import subprocess
import argparse
import os
import time

dim = 1000

files = glob.glob("./*")

print("files:", files)

outdir = f"../../small-jpg/{os.getcwd().split('/')[-1]}"

print("outdir:", outdir)
subprocess.run(f'mkdir {outdir}', shell=True)

print("setup done")
n = 0
ct = len(files)

startTime = time.monotonic()

for file in files:
    n += 1
    outfile = f'{file.split(".")[-2]}_{dim}.jpg'
    print(f"{n}/{ct}: {file} --> {outdir}{outfile}" )
    cmd = f'convert {file} -resize {dim}x{dim} {outdir}{outfile}'
    #print(cmd)
    subprocess.run(cmd, shell=True)
    dt = time.monotonic() - startTime 
    timeLeft =  (dt / n) * (ct-n)
    print(f"Time Left: {timeLeft} seconds")
    print(f"Time Left: {timeLeft/60} minutes")


# dir = f'{args.dir}*.{args.type}'
# dir = dir.replace("\\", "")

# print("dir: ", dir)
# print("type: ", args.type)

# outdir = f'{picdir}/'
# print(outdir)
# subprocess.run(f'mkdir {outdir}', shell=True)

# files = glob.glob(dir)

# #print(files)
# n = 0
# for f in files:
#     n += 1
#     f = f.replace(" ", "\ ")
#     print(f)
#     outName = f.split("/")[-2] + "_" + f.split("/")[-1]
#     outName = outdir + outName.replace(args.type, "png")
#     print(outName)
#     print(f'({n}/{len(files)})')
#     subprocess.run(f'convert {f} -resize 2000x2000 {outName}', shell=True)
