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
			

with open('smallercsv.csv') as source:
	reader = csv.reader(source)
	rows = []
	for row in reader: 
		rows.append(row)
	for i in range(1, len(OSLAUAs)):	
			for j in range(1,len(rows)):
				if OSLAUAs[i][1] == rows[j][1]:
					OSLAUAs[i].append(rows[j][2])

with open('smallercsv.csv') as source:
	reader = csv.reader(source)
	rows = []
	for row in reader: 
		rows.append(row)
	for i in range(1, len(CEDs)):	
			for j in range(1,len(rows)):
				if CEDs[i][1] == rows[j][0]:
					CEDs[i].append(rows[j][2])
					
listo = []
listc = []

for entry in OSLAUAs:
	listo.append([entry[0],entry[1],entry[2],entry[3]])

for entry in CEDs:
	listc.append([entry[0],entry[1],entry[2],entry[3]])

with open("osla", "x") as result:
	writer = csv.writer(result)
	for entry in listo:
		writer.writerow(entry)
		
with open("ceds", "x") as result:
	writer = csv.writer(result)
	for entry in listc:
		writer.writerow(entry)