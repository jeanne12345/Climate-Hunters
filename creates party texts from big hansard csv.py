#!/usr/bin/env python3

import csv
import string

from os import remove

def Flowercase(text):
	result = text.lower()
	return result

def Fpunctuation(text):
	punctuation = list(string.punctuation)
	punctuation.append('—')
	for mark in punctuation:
		text = text.replace(mark, ' ')
	return text


parties = ["Labour", "Conservative", "Liberal Democrat", "Green"]

def main(parties):
	party = str(parties)
	
	with open('hansard-speeches-v310.csv') as source:
		reader = csv.reader(source)
		
		file = open(f"{party}.txt", "x")
		for row in reader:
			if party in row[3]:
				file.write(f"{Flowercase(Fpunctuation(row[1]))}\n")
				
for i in parties:
	main(i)