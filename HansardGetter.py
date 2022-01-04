import csv

#MPname = str(input("mp name?"))
MPname = 'David Cameron'
fyear = int(input("starting date?"))
lyear = int(input("ending date?"))


with open('Hansard-speeches-v310.csv') as source:
    reader = csv.reader(source)


    with open(f"{MPname}_speeches.txt", "x")as result:
        writer = csv.writer(result)
        for row in reader:
            if row[17] == MPname:
                if int(row[13]) > fyear - 1 and int(row[13]) < (lyear) + 1:
                    writer.writerow(row[1])