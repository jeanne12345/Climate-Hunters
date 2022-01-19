#!/usr/bin/env python3


climlexgrp = ['sustainable', 'sustainability',  'climate change', 'climate crisis', 'climate disaster', 'climate conference', 'greenhouse effect', 'global warming', 'renewable energy', 'non-renewable energy', 'clean energy', 'renewable energy', 'green energy', 'sustainable energy', 'greenhouse gas' , 'emissions', 'carbon', 'oil spill', 'water pollution', 'water waste', 'conservation', 'biodiversity', 'clean air', 'air pollution', 'natural disaster', 'ozone', 'chemical waste', 'toxic chemicals', 'methane', 'ecosystem', 'habitat loss', 'habitat destruction', 'atmosphere', 'global climate', 'global warming', 'fossil fuels', 'fossil fuel', 'natural gas', 'fracking', 'greenhouse effect', 'UV radiation', 'ultraviolet radiation', 'renewable sources', 'drought', 'pollute', 'pollution', 'preservation', 'natural resources', 'energy supply', 'toxic waste', 'ecosystem', 'environmental', 'natural environment', 'ecological', 'ecology', 'pollutant', 'nuclear power', 'solar power', 'wind power', 'biomass', 'windpower', 'biomass', 'aerosols', 'rising temperature', 'rising temperatures', 'power source', 'gases', 'radiation', 'fuels', 'species', 'extinction', 'climate convention', 'Kyoto protocol', 'unfcc', 'atmospheric', 'infrared', 'climate system', 'kyoto', 'deforestation', 'environmental protection', 'natural resources', 'ipcc', 'extreme weather', 'air pollution', 'ecosystem', 'radiative', 'organisms', 'gas emission', 'sea level', 'COP', 'electricity', 'recycling', 'green transport' , 'electric vehicles', 'hybrid vehicle', 'hybrid car', 'hybrid bus']


partyfilelist = ['Liberal Democrat.txt', 'Green.txt', 'Conservative.txt', 'Labour.txt']

def instancecounter(text,ngram):
	count = 0
	for i in range(0,len(text)):
		if text[i:i+(len(ngram))] == ngram:
			count+=1
	return count

for ngram in climlexgrp:
	print(ngram)

for party in partyfilelist:
	print("start", party)
	filename = party
	file = open(filename, 'rt')
	text = file.read()
	file.close()
	for ngram in climlexgrp:
		print(instancecounter(text,ngram))
	print("end", party)
	print("\n\n'")