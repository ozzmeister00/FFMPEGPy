"""

"""
import ffmpyg.ffmpyg


def concat(inFileListPath, outputFilePath, doWait=False):
    """
    Concatenates files of the same codec into a single file

    :param str inFileListPath: path to the file containing a list of files to concatenate
    :param str outputFilePath: path to which to write the concatenated file
    :param bool doWait: if true, will wait for the subprocess to finish

    :return bool: success of the operation
    """
    return ffmpyg.ffmpyg.run("-f", "concat", "-y", '-safe', '0', '-i', "{}".format(inFileListPath), '-vcodec', 'copy',
                             '-acodec', 'copy', "{}".format(outputFilePath), doWait=doWait)
