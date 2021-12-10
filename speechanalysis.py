import csv
from os import remove
 
 
def remove_dashes(string):
   result = string.replace('-', '')
   return int(result)
 
 
def main():
   MPname = str(input("mp name?"))
   fdate = int(input("starting date?"))
   ldate = int(input("ending date?"))
 
   with open('hansard-speeches-v310.csv') as source:
       reader = csv.reader(source)
 
       file = open(f"{MPname}_speeches.txt", "x")
       for row in reader:
           if row[17] == MPname:
               if remove_dashes(row[6]) > fdate - 1 and remove_dashes(row[6]) < ldate + 1:
                   file.write(f"{row[1]}\n")
 
 
if __name__ == "__main__":
   main()
 
 

