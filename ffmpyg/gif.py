import ffmpyg.ffmpyg

def mp4ToGif(inputFile, framerate, scale, duration, loop, outputPath, doWait=False):
    """

    :param str inputFile: path to the input file
    :param int framerate: framerate of the output gif
    :param int scale: width of the output gif
    :param int duration: how long the resulting gif should be, if -1 will skip
    :param bool loop: if true, will set the gif to looping
    :param str outputPath: path to which to output the file
    :param bool doWait: if true, will wait for the operation to finish
    :return bool: success of the operation
    """
    return ffmpyg.ffmpyg.run("-t", str(duration), '-i', "{}".format(inputFile), '-vf',
                             'fps={0},scale={1}:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse'.format(framerate, scale),
                             '-loop', str(int(loop)), "{}".format(outputPath), doWait=doWait)
