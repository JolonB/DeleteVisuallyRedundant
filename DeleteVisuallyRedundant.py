#!/usr/bin/env python3

import getopt  # TODO argparse
import os
import re
import sys  # TODO remove when switched to argparse

dupsFile = "dups.txt"  # TODO why isn't this const?
filepath = None  # TODO why is this global???
toRemoveDupFile = True  # TODO change everything to snake_case
toDryRun = False
opts, args = getopt.getopt(sys.argv[1:], "p:rd")

for o, a in opts:
	if o == "-p":
		filepath = a
	elif o == "-r":
		toRemoveDupFile = False
	elif o == "-d":
		toDryRun = True

# TODO `if not filepath`
if filepath == None:
	print("Error: Please provide path using the -p option")
	exit()

# TODO can this be run using Python instead of system calls?
os.system("findimagedupes -R \"{}\" > \"{}\"".format(filepath, dupsFile))

def deleteAllButLargestAndOldest(filepaths):
	# TODO add comments!!
	maxSize = 0
	maxFilepaths = []
	remainingFilepaths = []

	# TODO tidy all of this up
	for filepath in filepaths:
		size = os.stat(filepath).st_size
		if (size > maxSize):
			maxSize = size

	for filepath in filepaths:
		size = os.stat(filepath).st_size

		if(size < maxSize):
			print("D:", filepath)
			if toDryRun == False:
				os.remove(filepath)
		elif (size == maxSize):
			maxFilepaths.append(filepath)

	if (len(maxFilepaths) > 1):
		oldestModifiedTime = float("inf")

		for filepath in maxFilepaths:
			modifiedTime = os.stat(filepath).st_mtime

			if (modifiedTime < oldestModifiedTime):
				oldestModifiedTime = modifiedTime

		for filepath in maxFilepaths:
			modifiedTime = os.stat(filepath).st_mtime

			if(modifiedTime > oldestModifiedTime):
				print("D:", filepath)
				if toDryRun == False:
					os.remove(filepath)
			elif (modifiedTime == oldestModifiedTime):
				remainingFilepaths.append(filepath)

	# Remove all but one duplicate if any still exist
	for filepath in remainingFilepaths[1:]:
		if toDryRun == False:
			os.remove(filepath)

# TODO def main() and if __name__ == "__main__"
# TODO maybe make this global
filename_regex = re.compile("(.+?\.(?:jpe?g|png|gif))(?:\s+|$)", flags=re.IGNORECASE)
with open(dupsFile, 'r') as fp:
	# TODO why are we enumerating??
	for cnt, line in enumerate(fp):
		matches = filename_regex.findall(line)

		deleteAllButLargestAndOldest(matches)

if toRemoveDupFile:
	os.remove(dupsFile)

