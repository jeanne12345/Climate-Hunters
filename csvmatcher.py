#!/usr/bin/env python3


import csv

OSLAUAs = [['year', 'code', 'recycling']]
CEDs = [['year', 'code', 'recycling']]
Cities = [['year', 'code', 'recycling']]


with open('year_code_recycling.csv') as source:
	reader = csv.reader(source)
	for row in reader:
		if "E06" in row[1]:
			OSLAUAs.append([row[0], row[1], row[2]])
		elif "E07" in row[1]:
			OSLAUAs.append([row[0], row[1], row[2]])
		elif "E08" in row[1]:
			OSLAUAs.append([row[0], row[1], row[2]])
		elif "E09" in row[1]:
			OSLAUAs.append([row[0], row[1], row[2]])
		elif "E10" in row[1]:
			CEDs.append([row[0], row[1], row[2]])
		elif "E50" in row[1]:
			Cities.append([row[0], row[1], row[2]])



file = open('ONSPD_NOV_2021_UK.csv')
type(file)
csvreader = csv.reader(file)
	
with open("smallercsv", "x")as result:
	writer = csv.writer(result)
	for row in csvreader:
		writer.writerow([row[6],row[7],row[19]])
