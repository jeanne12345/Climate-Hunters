#!/usr/bin/env python3

import csv

OSLAUAs = [['year', 'code', 'recycling']]


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
			
with open('smallercsv2.csv') as source:
	reader = csv.reader(source)
	rows = []
	for row in reader: 
			rows.append(row)
	for i in range(1, len(OSLAUAs)):	
		for j in range(1,len(rows)):
			if OSLAUAs[i][1] == rows[j][1]:
				OSLAUAs[i].append(rows[j][2])
				
with open("oslaua.csv", "x") as result:
	writer = csv.writer(result)
	for row in OSLAUAs: 
		writer.writerow(row)