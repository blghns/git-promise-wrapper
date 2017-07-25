import argparse
import os
import subprocess

gitCommand = "git diff --unified=0 dd91b1e3085a760f099d7667233781ea1dd0ff45 file1.py | grep '@@' | awk '{print $2}' | tr -d -"


def checkPromise(fileName):
	promisedLines = [1,5,7]
	promisedLinesBetween = ['10-15',]
	process = subprocess.Popen(gitCommand.split(),
                               cwd=os.getcwd(),
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
	output, error = process.communicate()
	linesEdited = output.split()

	for lineEdited in linesEdited:
		if "," in lineEdited:
			lineEdited = lineEdited.split(',')
			if lineEdited[1] == 0:
				if not checkLine(lineEdited[0]):
					return False
			else:
				lineEdited = lineEdited[0]+'-'+lineEdited[1]
				for promisedRange in promisedLinesBetween:
					if not checkRanges(lineEdited, promisedRange):
						return False
		elif not checkLine(lineEdited, promisedLines) and not checkPromisedRange(lineEdited, promisedLinesBetween):
			return False
	return True

def checkLine(lineEdited, promisedLines):
	if not int(lineEdited) in promisedLines:
		return False
	return True

def checkPromisedRange(lineEdited, promisedRange):
	for promisedRange in promisedRange:
		linedEdited = int(lineEdited)
		promisedStart = int(promisedRange.split("-")[0])
		promisedEnd = int(promisedRange.split("-")[1])
		range = promisedRange.split("-")
		if  not promisedStart-linedEdited <= 0 and promisedEnd - linedEdited >= 0:
			return False
	return True

def checkRanges(editedRange, promisedRange):
	promisedStart = int(promisedRange.split("-")[0])
	promisedEnd = int(promisedRange.split("-")[1])
	editedStart = int(editedRange.split("-")[0])
	editedEnd = int(editedRange.split("-")[1])
	if promisedStart - editedStart <= 0 and promisedEnd - editedEnd >= 0:
		return True
	return False

print "Checking if promise was kept..."

if checkPromise("file1.py"):
	print "\nPromise was kept. Commiting changes."
else:
	print "\nPromise not kept. Changes will not be commited."
