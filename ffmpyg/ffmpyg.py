"""

"""
import subprocess
import sys

from . import _binaryLocation


def run(*args, **kwargs):
    print(*args)
    process = subprocess.Popen([_binaryLocation, *args], shell=True)

    #for c in iter(lambda: process.stdout.read(1), b""):
     #   print(c.decode('ascii'))
        #sys.stdout.buffer.write(c)

    if "doWait" in kwargs:
        if kwargs["doWait"]:
            process.wait()

    output, error = process.communicate()

    if output:
        print("STDOUT\n", output.decode('ascii'))
    if error:
        print("STDERR\n", error.decode('ascii'))
        return False

    return True
