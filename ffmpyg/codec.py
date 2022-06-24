"""

"""
import ffmpyg.ffmpyg


def updateCodecs(inputFile, outputFile, videoCodec=None, audioCodec=None, doWait=False):
    """
    Changes the codecs of the input file to the provided codecs and outputs that to outputfile
    :param inputFile:
    :param outputFile:
    :param videoCodec:
    :param audioCodec:
    :param bool doWait:
    """
    args = ['-i', inputFile]
    if videoCodec:
        args += ['-vcodec', videoCodec]
    if audioCodec:
        args += ['-acodec', audioCodec]
    args.append(outputFile)

    ffmpyg.ffmpyg.run(*args, doWait=doWait)

