#!/usr/bin/env python3


climlexgrp = ['sustainable', 'sustainability',  'climate change', 'climate crisis', 'climate disaster', 'climate conference', 'greenhouse effect', 'global warming', 'renewable energy', 'non-renewable energy', 'clean energy', 'renewable energy', 'green energy', 'sustainable energy', 'greenhouse gas' , 'emissions', 'carbon', 'oil spill', 'water pollution', 'water waste', 'conservation', 'biodiversity', 'clean air', 'air pollution', 'natural disaster', 'ozone', 'chemical waste', 'toxic chemicals', 'methane', 'ecosystem', 'habitat loss', 'habitat destruction', 'atmosphere', 'global climate', 'global warming', 'fossil fuels', 'fossil fuel', 'natural gas', 'fracking', 'greenhouse effect', 'UV radiation', 'ultraviolet radiation', 'renewable sources', 'drought', 'pollute', 'pollution', 'preservation', 'natural resources', 'energy supply', 'toxic waste', 'ecosystem', 'environmental', 'natural environment', 'ecological', 'ecology', 'pollutant', 'nuclear power', 'solar power', 'wind power', 'biomass', 'windpower', 'biomass', 'aerosols', 'rising temperature', 'rising temperatures', 'power source', 'gases', 'radiation', 'fuels', 'species', 'extinction', 'climate convention', 'Kyoto protocol', 'unfcc', 'atmospheric', 'infrared', 'climate system', 'kyoto', 'deforestation', 'environmental protection', 'natural resources', 'ipcc', 'extreme weather', 'air pollution', 'ecosystem', 'radiative', 'organisms', 'gas emission', 'sea level', 'COP', 'electricity', 'recycling', 'green transport' , 'electric vehicles', 'hybrid vehicle', 'hybrid car', 'hybrid bus']

mpfilelist = ['Amber Rudd_20160713_20180429.txt', 'Boris Johnson_20160713_20180709.txt', 'Boris Johnson_20190724_20200831.txt', 'David Cameron_20100511_20160713.txt', 'Dominic Raab_20190724_20200831.txt', 'George Osborne_20100512_20160713.txt', 'Jeremy Hunt_20180709_20190724.txt', 'Philip Hammond_20160713_20190724.txt', 'Priti Patel_20190724_20200831.txt', 'Rishi Sunak_20200213_20200831.txt', 'Sajid Javid_20180430_20190724.txt', 'Sajid Javid_20190724_20200213.txt', 'Theresa May_20100512_20160713.txt', 'Theresa May_20160713_20190724.txt', 'William Hague_20100512_20140714.txt']


def instancecounter(text,ngram):
	count = 0
	for i in range(0,len(text)):
		if text[i:i+(len(ngram))] == ngram:
			count+=1
	return count

for mp in mpfilelist:
	filename = mp
	file = open(filename, 'rt')
	text = file.read()
	file.close()
	for ngram in climlexgrp:
		print(instancecounter(text,ngram), ngram)
	