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

listoftupls = [["Alan Johnson", 20101008, 20110120], ["Ed Balls", 20110120, 20150511], ["Chris Leslie", 20150511, 20150912], ["John McDonnell", 20150913, 20200405], ["David Miliband", 20100511, 20101008], ["Yvette Cooper", 20101008, 20110120], ["Douglas Alexander", 20110120, 20150511], ["Hilary Benn", 20150511, 20160626], ["Emily Thornberry", 20160627, 20200101], ["Alan Johnson", 20100511, 20101008], ["Ed Balls", 20101008, 20110120], ["Yvette Cooper", 20110120, 20150912], ["Andy Burnham", 20150913, 20160928], ["Diane Abbott", 20161006, 20100405]]

def main(tupl):
    MPname = str(tupl[0])
    fdate = int(tupl[1])
    ldate = int(tupl[2])

    with open('hansard-speeches-v310.csv') as source:
        reader = csv.reader(source)

        file = open(f"{MPname}_{fdate}_{ldate}0.txt", "x")
        for row in reader:
            if MPname in row[17]:
                if remove_dashes(row[6]) > fdate - 1 and remove_dashes(row[6]) < ldate + 1:
                    file.write(f"{Flowercase(Fpunctuation(row[1]))}\n")

for i in listoftupls:
    main(i)