#!/usr/bin/env python3

filelist = ['Alan Johnson_20100511_20101008.txt', 'Alan Johnson_20101008_20110120.txt', 'Amber Rudd_20160713_20180429.txt',  'Andy Burnham_20150913_20160928.txt', 'Anneliese Dodds_20200405_20200831.txt', 'Boris Johnson_20160713_20180709.txt', 'Boris Johnson_20190724_20200831.txt', 'Chris Leslie_20150511_20150912.txt', 'David Cameron_20100511_20160713.txt', 'David Miliband_20100511_20101008.txt', 'Diane Abbott_20161006_20200405.txt', 'Dominic Raab_20190724_20200831.txt', 'Douglas Alexander_20110120_20150511.txt', 'Ed Balls_20101008_20110120.txt', 'Ed Balls_20110120_20150511.txt', 'Edward Miliband_20100925_20150508.txt', 'Emily Thornberry_20160627_20200101.txt', 'George Osborne_20100512_20160713.txt', 'Harriet Harman_20100511_20200925.txt', 'Harriet Harman_20150815_20150912.txt', 'Hilary Benn_20150511_20160626.txt', 'Jeremy Corbyn_20150912_20200404.txt', 'Jeremy Hunt_20180709_20190724.txt', 'John McDonnell_20150913_20200405.txt', 'Keir Starmer_20200404_20200831.txt', 'Philip Hammond_20160713_20190724.txt', 'Priti Patel_20190724_20200831.txt', 'Rishi Sunak_20200213_20200831.txt', 'Sajid Javid_20180430_20190724.txt', 'Sajid Javid_20190724_20200213.txt', 'Theresa May_20100512_20160713.txt', 'Theresa May_20160713_20190724.txt', 'William Hague_20100512_20140714.txt', 'Yvette Cooper_20101008_20110120.txt', 'Yvette Cooper_20110120_20150912.txt']

#filelist = ["Labour", "Conservative", "Liberal Democrat", "Green"]


for i in filelist:
	print("start", i)
	filename = i
	file = open(filename, 'rt')
	text = file.read()
	file.close()
	print(len(text.split()))
	print("end", i)
	print("\n\n'")
	