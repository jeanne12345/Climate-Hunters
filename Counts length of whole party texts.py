#!/usr/bin/env python3

		
		
partyfilelist = ['Liberal Democrat.txt', 'Green.txt', 'Conservative.txt', 'Labour.txt']


for party in partyfilelist:
	filename = party
	file = open(filename, 'rt')
	text = file.read()
	file.close()
	text.split()
	print(party)
	print(len(text))