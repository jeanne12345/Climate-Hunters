import nltk
from nltk.tokenize import sent_tokenize
import string

#inp = input("phrase?")
#ngram = inp.split()

climlexgrp = ['Climate change', 'greenhouse effect', 'global warming', 'renewable energy', 'non-renewable energy','energy', 'climate', 'waste', 'water', 'conservation', 'biodiversity', 'air', 'disaster', 'forest', 'tsunami', 'earthquake', 'hurricane', 'natural disaster', 'ozone', 'chemicals', 'soil', 'methane', 'Ecosystems ', 'habitat', 'Atmosphere', 'weather', 'Global Climate', 'Fossil fuel', 'coal ', 'oil', 'natural gas', 'water vapour', 'carbon dioxide', 'carbon ', 'Greenhouse effect', 'ultraviolet radiation', 'global warming ', 'carbon footprint', 'renewable sources', 'drought', 'pollute', 'wilderness preservation', 'pollution', 'preservation', 'natural resources', 'energy supply', 'toxic wastes', 'ecosystem', 'environmental', 'environment ', 'ecological ', 'ecology', 'pollutant', 'nature ', 'earth', 'nuclear power', 'solar power ', 'wind power ', 'biomass', 'ocean', 'aerosols', 'temperatures', 'temperature ', 'power', 'sources', 'gases', 'radiation', 'andor', 'natural', 'greenhouse effect', 'dioxide', 'anthropogenic', 'fossil', 'ghg', 'earths surface', 'fuels', 'soil', 'species', 'convention climate', 'ice', 'Kyoto protocol', 'unfcc', 'atmospheric', 'infrared', 'climate system', 'kyoto', 'protocol', 'forest', 'ipcc', 'weather', 'land ', 'air', 'ecosystem', 'radiative', 'organisms', 'gas emission', 'deforestation', 'sea level', 'plants', 'petroleum', 'COP', 'electricity', 'recycling', 'sustainable', 'sustainability']


# load text
filename = 'Jeremy_Corbyn_speeches3.txt'
file = open(filename, 'rt')
text = file.read()
file.close()


def Flowercase(text):
    result = text.lower()
    return result

def Fpunctuation(text):
    punctuation = list(string.punctuation)
    punctuation.append('—')
    for mark in punctuation:
        text = text.replace(mark, ' ')
    return text


resul = Fpunctuation(Flowercase(text))
result = (resul.split())


def instancecounter(text,ngram):
    count = 0
    for i in range(0,len(text)):
        if text[i:i+(len(ngram))] == ngram:
            count+=1
    return count


def KWIC(text, ngram):
    m = 4
    dubs =[]
    for i in range(0, len(text)):
        if text[i:i + (len(ngram))] == ngram:
            dubs.append((text[i - m:i + (len(ngram) + m)]))
    return dubs


for ngram in climlexgrp:
    phrase = ngram.split()
    for sent in (KWIC(result,phrase)):
        print(sent)

