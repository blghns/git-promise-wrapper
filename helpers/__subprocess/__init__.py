import subprocess
import os


def make_call(command):
    if type(command) is str:
        command = command.split()
    process = subprocess.Popen(command,
                               cwd=os.getcwd(),
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        raise error
    return output
