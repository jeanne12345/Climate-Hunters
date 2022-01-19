#!/usr/bin/env python3
		
import csv

CEDs = [['year', 'code', 'recycling']]


with open('year_code_recycling.csv') as source:
	reader = csv.reader(source)
	for row in reader: 
		if "E10" in row[1]:
			CEDs.append([row[0], row[1], row[2]])
		elif "E50" in row[1]:
			CEDs.append([row[0], row[1], row[2]])
		
			
with open('smallercsv2.csv') as source:
	reader = csv.reader(source)
	rows = []
	for row in reader: 
			rows.append(row)
	for i in range(1, len(CEDs)):	
		for j in range(1,len(rows)):
			if CEDs[i][1] == rows[j][1]:
				CEDs[i].append(rows[j][2])
				
with open("ced.csv", "x") as result:
	writer = csv.writer(result)
	for row in CEDs: 
		writer.writerow(row)