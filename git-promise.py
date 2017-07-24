import argparse
import helpers.promise
import helpers.git
from helpers import parseFileArgs

parser = argparse.ArgumentParser(description='Promise lines in git. GitVow backbone.')
parser.add_argument('newBranchName', metavar='branch',
                    help='Name of the promise branch, if promise branch exist, append new promise lines.\n')

group = parser.add_argument_group('optional line selection')
group.add_argument('-f', '--file', metavar='name', dest='file', required=True, nargs='+',
                   action=parseFileArgs.customParser,
                   help='Name of the file to be promised. This file will be editable in the promised branch, but will not be editable in the parent branch.\n')
group.add_argument('-l', '--lines', metavar='N', dest='lines', nargs='+', type=int, action='append',
                   help='Lines in the specified file to be promised. If not specified, all file will be promised.\n')
group.add_argument('-b', '--between', metavar='N-N', dest='linesInBetween', nargs='+', action='append',
                   help='Specify the range of lines to be promised in the selected file.\n')

args = parser.parse_args(
    "newBranch -f myFile1 -l 1 3 5 -b 15-20 30-40 -f myFile2 -l 3 5 -l 7 -b 40 50 -l 10 -f myfile3 -f yolo/myfile4".split(
        " "))

parseFileArgs.customParser.finalize(args)
print args

if not helpers.git.branch_exists(args.newBranchName):
    helpers.promise.write_promise(args)
    helpers.git.add(".promise")
    helpers.git.commit("New promise for branch: " + args.newBranchName + " is created")
    helpers.git.branch(args.newBranchName)
