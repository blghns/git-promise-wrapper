import argparse
import os
import subprocess

git_command = "git diff --unified=0 dd91b1e3085a760f099d7667233781ea1dd0ff45 file1.py | grep '@@' | awk '{print $2}' | tr -d -"


def check_promise(file_name):
    promised_lines = [1, 5, 7]
    promised_lines_between = ['10-15', ]
    process = subprocess.Popen(git_command.split(),
                               cwd=os.getcwd(),
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    output, error = process.communicate()
    lines_edited = output.split()

    for line_edited in lines_edited:
        if "," in line_edited:
            line_edited = line_edited.split(',')
            if line_edited[1] == 0:
                if not check_line(line_edited[0]):
                    return False
            else:
                line_edited = line_edited[0] + '-' + line_edited[1]
                for promisedRange in promised_lines_between:
                    if not check_ranges(line_edited, promisedRange):
                        return False
        elif not check_line(line_edited, promised_lines) and not check_promised_range(line_edited, promised_lines_between):
            return False
    return True


def check_line(line_edited, promised_lines):
    if not int(line_edited) in promised_lines:
        return False
    return True


def check_promised_range(line_edited, promised_range):
    for promised_range in promised_range:
        lined_edited = int(line_edited)
        promised_start = int(promised_range.split("-")[0])
        promised_end = int(promised_range.split("-")[1])
        promise_range = promised_range.split("-")
        if not promised_start - lined_edited <= 0 and promised_end - lined_edited >= 0:
            return False
    return True


def check_ranges(edited_range, promised_range):
    promised_start = int(promised_range.split("-")[0])
    promised_end = int(promised_range.split("-")[1])
    edited_start = int(edited_range.split("-")[0])
    edited_end = int(edited_range.split("-")[1])
    if promised_start - edited_start <= 0 <= promised_end - edited_end:
        return True
    return False


print "Checking if promise was kept..."

if check_promise("file1.py"):
    print "\nPromise was kept. Committing changes."
else:
    print "\nPromise not kept. Changes will not be committed."
