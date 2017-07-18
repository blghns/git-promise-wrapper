import argparse


parser = argparse.ArgumentParser(description='Promise lines in git. GitVow backbone.')

parser.add_argument('newBranchName', metavar='branch', help='Name of the promise branch, if promise branch exist, append new promise lines.\n')


group = parser.add_argument_group('optional line selection')

group.add_argument('-f', '--file', metavar='name', dest='filesAndLines', required=True,nargs='+', action='append', help='Name of the file to be promised. This file will be editable in the promised branch, but will not be editable in the parent branch.\n')

group.add_argument('-l', '--lines', metavar='N', dest='filesAndLines', nargs='+', type=int, action='append', help='Lines in the specified file to be promised. If not specified, all file will be promised.\n')

group.add_argument('-b', '--between', metavar='N-N', dest='filesAndLines', nargs='+', action='append', help='Specify the range of lines to be promised in the selected file.\n')


args = parser.parse_args()

print args

