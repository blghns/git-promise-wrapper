import argparse
import subprocess

gitCommand = "git diff --unified=0 dd91b1e3085a760f099d7667233781ea1dd0ff45 file1.py | grep '@@' | awk '{print $2}' | tr -d -"


def checkPromise(fileName):
	promisedLines = [5, 7]
	promisedLinesBetween = ['10-15',]
	process = subprocess.Popen(gitCommand.split(), stdout=subprocess.PIPE, shell=True)
	output, error = process.communicate()
	linesEdited = map(int, output.split())
	for lineEdited in linesEdited:
		if not checkLine(lineEdited, promisedLines) and not checkRange(lineEdited, promisedLinesBetween):
			print "--- Check Lines: "+str(checkLine(lineEdited, promisedLines))
			print "--- Check Range: "+str(checkRange(lineEdited, promisedLinesBetween))
			return False
	return True

def checkLine(lineEdited, promisedLines):
	print "checking lines"
	if not lineEdited in promisedLines:
		print "Edited: "+str(lineEdited)
		return False
	return True

def checkRange(lineEdited, promisedLinesBetween):
	print "checking ranges"
	for promisedRange in promisedLinesBetween:
		range = promisedRange.split("-")
		if  not int(range[0])-lineEdited <= 0 and int(range[0]) - lineEdited >= 0:
			print "Edited"+str(lineEdited)
			print "Promised"+str(promisedRange)
			return False
	return True

print "Checking if promise was kept..."

if checkPromise("file1.py"):
	print "\nPromise was kept. Commiting changes."
else:
	print "\nPromise not kept. Changes will not be commited."
