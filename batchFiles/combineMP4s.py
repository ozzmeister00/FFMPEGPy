import sys
import os
import ffmpyg.concat


def writeOutputFile(targetFolder, filePathList):
    """

    :param str targetFolder:
    :param srt filePathList:
    :return str: path to the output file list
    """
    outStr = ""
    for filePath in filePathList:
        filePath = filePath.replace('\\', '/')  # concat expects forward slashes!
        if ' ' in filePath:
            filePath = '"{}"'.format(filePath)
        outStr += "file " + filePath + '\n'

    outFile = os.path.join(targetFolder, "fileList.txt")
    with open(outFile, 'w') as fh:
        fh.write(outStr)

    return outFile


def parseForFiles(targetFolder, targetExtension):
    """

    :param str targetFolder: the director to parse
    :param str targetExtension: the extension to parse for
    :return list[str]: full file paths in the target folder which end in the input extension
    """
    outList = []
    for filename in os.listdir(targetFolder):
        print(filename)
        if filename.lower().endswith(targetExtension):
            print(filename)
            outList.append(os.path.join(targetFolder, filename))

    return outList


def Main(targetFolder, targetExtension, outputFile, doWait=False):
    """
    Searches the input folder for files with the input extension and greats a file
    to store those file names before passing it off to ffmpeg's concat
    command

    :param str targetFolder: the director to parse
    :param str targetExtension: the extension to parse for
    :param str outputFile: path to the file to which you'd like to output
    :param bool doWait: if true, will wait for the subprocess to finish

    :return bool: success of the operation
    """
    fileList = parseForFiles(targetFolder, targetExtension)
    fileListPath = writeOutputFile(targetFolder, fileList)
    fileListPath = fileListPath.replace('\\', '/')
    if ffmpyg.concat.concat(fileListPath, outputFile, doWait=doWait):
        # clean up after yourself if successful, otherwise leave the junk in place for debugging
        os.unlink(fileListPath)
        return True

    return False


if __name__ == "__main__":
    # todo swap this for argparse
    if len(sys.argv) > 1:
        targetFolder = sys.argv[1]
        targetExtension = sys.argv[2]
        outputFile = sys.argv[3]
    else:
        targetFolder = "G:/GoPro/2018-08-24/HERO5_Session_1"
        targetExtension = ".mp4"
        outputFile = "G:/GoPro/batched/commutes/2018_08_24_commute.mp4"

    Main(targetFolder, targetExtension, outputFile)
