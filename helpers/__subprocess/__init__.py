import subprocess
import os


def call(command, shell=False):
    if type(command) is str:
        command = command.split()
    process = subprocess.Popen(command,
                               shell=shell,
                               cwd=os.getcwd(),
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    output, error = process.communicate()
    #if error:
    #    raise error
    return output
