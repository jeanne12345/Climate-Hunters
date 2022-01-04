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

def remove_dashes(string):
    result = string.replace('-', '')
    return int(result)

listoftupls = [["David Cameron", 20100511, 20160713], ["Theresa May", 20160713, 20190724], ["Boris Johnson", 20190724, 20200831], ["George Osborne", 20100512, 20160713], ["Philip Hammond", 20160713, 20190724], ["Sajid Javid", 20190724, 20200213], ["Rishi Sunak", 20200213, 20200831], ["William Hague", 20100512, 20140714], ["Boris Johnson", 20160713, 20180709], ["Jeremy Hunt", 20180709, 20190724], ["Dominic Raab", 20190724, 20200831], ["Theresa May", 20100512, 20160713], ["Amber Rudd", 20160713, 20180429], ["Sajid Javid", 20180430, 20190724], ["Priti Patel", 20190724, 20200831]]

def main(tupl):
    MPname = str(tupl[0])
    fdate = int(tupl[1])
    ldate = int(tupl[2])

    with open('hansard-speeches-v310.csv') as source:
        reader = csv.reader(source)

        file = open(f"{MPname}_{fdate}_{ldate}.txt", "x")
        for row in reader:
            if row[17] == MPname:
                if remove_dashes(row[6]) > fdate - 1 and remove_dashes(row[6]) < ldate + 1:
                    file.write(f"{Flowercase(Fpunctuation(row[1]))}\n")

for i in listoftupls:
    main(i)