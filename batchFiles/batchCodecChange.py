import logging
import os

import ffmpyg.codec

inDirectory = "G:\\GoPro\\Batched"

logging.basicConfig(filename=os.path.join(inDirectory, "batchCodecChange.log"), encoding='utf-=8', level=logging.DEBUG)

batchFiles = []

for dirPath, dirNames, files in os.walk(inDirectory):
    for filename in files:
        if filename.lower().endswith('.mp4'):
            outFilename, ext = os.path.splitext(filename)
            outFilename += "_compressed" + ext
            batchFiles.append((os.path.join(dirPath, filename), os.path.join(dirPath, outFilename)))
try:
    for inFile, outFile in batchFiles:
        logging.info("Converting {} to {}".format(inFile, outFile))
        ffmpyg.codec.updateCodecs(inFile, outFile, 'h264', 'mp2', doWait=True)
except Exception as e:
    logging.error("Error encountered")
    logging.error(e)

logging.info("Done!")
