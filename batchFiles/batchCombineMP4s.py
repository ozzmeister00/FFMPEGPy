import combineMP4s
import os

inFile = r"G:\GoPro\batch.csv"

with open(inFile, 'r') as fh:
    for line in fh.readlines():
        inFolder, outFile = line.split(',')
        inFolder = inFolder.replace('\\', '/').replace(' ', '_')  # for safety
        outFile = outFile.replace('\\', '/').strip()  # for safety
        print("Concating mp4s in {} to {}".format(inFolder, outFile))
        combineMP4s.Main(inFolder, '.mp4', outFile, doWait=True)

print("done!")
