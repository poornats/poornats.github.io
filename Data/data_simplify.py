# -*- coding: utf-8 -*-

import pprint
import csv

import json
import codecs


from datetime import datetime, timedelta        


import pandas as pd

df = pd.read_csv('MotherJones_original.csv')

df.drop_duplicates().to_csv('MotherJones_original_no_dups.csv', index=False)



years = ["1982","1983","1984","1985","1986","1987","1988","1989","1990", "1991","1992", "1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]

with open('MotherJones_final.csv', mode='w') as syncHR:
    mapping_writer = csv.writer(syncHR, delimiter=',')

    mapping_writer.writerow(["Year", "Number_of_incidents", "Wounded", "Killed"])

    
    for year in years:
        incident_count = 0
        wounded_count = 0
        killed_count = 0
        with open('MotherJones_original_no_dups.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print( row[23],year )
                if row[23] == year:
                    incident_count = incident_count + 1
                    if row[5].isnumeric() == True:
                        wounded_count = wounded_count + int(row[5])
                    
                    killed_count = killed_count + int(row[4])
                    
            
        mapping_writer.writerow([year, incident_count, wounded_count, killed_count])
        print(year, incident_count, wounded_count, killed_count)




#############################################################################


with open('GVA_data/GunViolenceArchive.csv', mode='w') as syncHR:
    mapping_writer = csv.writer(syncHR, delimiter=',')

    mapping_writer.writerow(["Incident ID",	"Incident Date","State","City Or County","Address",	"# Killed",	"# Injured","Operations"])

    with open('GVA_data/GVA_all.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # i =0
        prev_year = 0
        for row in readCSV:
            if row[0]=="Incident ID":
                print(row[0])
            else:
                mapping_writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])

    with open('GVA_data/GVA_2019.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # i =0
        prev_year = 0
        for row in readCSV:
            if row[0]=="Incident ID":
                print(row[0])
            else:
                mapping_writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])

    with open('GVA_data/GVA_2018.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # i =0
        prev_year = 0
        for row in readCSV:
            if row[0]=="Incident ID":
                print(row[0])
            else:
                mapping_writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])

    with open('GVA_data/GVA_2017.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # i =0
        prev_year = 0
        for row in readCSV:
            if row[0]=="Incident ID":
                print(row[0])
            else:
                mapping_writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])
                
    with open('GVA_data/GVA_2016.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # i =0
        prev_year = 0
        for row in readCSV:
            if row[0]=="Incident ID":
                print(row[0])
            else:
                mapping_writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])

    with open('GVA_data/GVA_2015.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # i =0
        prev_year = 0
        for row in readCSV:
            if row[0]=="Incident ID":
                print(row[0])
            else:
                mapping_writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])


    with open('GVA_data/GVA_2014.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # i =0
        prev_year = 0
        for row in readCSV:
            if row[0]=="Incident ID":
                print(row[0])
            else:
                mapping_writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])


df = pd.read_csv('GVA_data/GunViolenceArchive.csv')

df.drop_duplicates().to_csv('GVA_data/GunViolenceArchive_no_dups.csv', index=False)


##################################################

years = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]

with open('GVA_final.csv', mode='w') as syncHR:
    mapping_writer = csv.writer(syncHR, delimiter=',')

    mapping_writer.writerow(["Year", "Number_of_incidents", "Wounded", "Killed"])

    
    for year in years:
        incident_count = 0
        wounded_count = 0
        killed_count = 0
        with open('GVA_data/GunViolenceArchive_no_dups.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print( row[1][len(row[1])-4:len(row[1])],year )
                if(row[1][len(row[1])-4:len(row[1])]) == year:
                    incident_count = incident_count + 1
                    wounded_count = wounded_count + int(row[6])
                    killed_count = killed_count + int(row[5])
            
        mapping_writer.writerow([year, incident_count, wounded_count, killed_count])
        print(year, incident_count, wounded_count, killed_count)
    

##################################################
df = pd.read_csv('everytown.csv')

df.drop_duplicates().to_csv('everytown_no_dups.csv', index=False)


years = ["2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]

with open('everytown_final.csv', mode='w') as syncHR:
    mapping_writer = csv.writer(syncHR, delimiter=',')

    mapping_writer.writerow(["Year", "Number_of_incidents", "Wounded", "Killed"])

    
    for year in years:
        incident_count = 0
        wounded_count = 0
        killed_count = 0
        with open('everytown_no_dups.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print( row[0][0:4],year )
                if row[0][0:4] == year:
                    incident_count = incident_count + 1
                    wounded_count = wounded_count + int(row[7])
                    killed_count = killed_count + int(row[6])

            
        mapping_writer.writerow([year, incident_count, wounded_count, killed_count])
        print(year, incident_count, wounded_count, killed_count)



###############################################################



with open('MST_final.csv', mode='w') as syncHR:
    mapping_writer = csv.writer(syncHR, delimiter=',')

    mapping_writer.writerow(["Year", "Number_of_incidents", "Wounded", "Killed"])

    data=json.load(codecs.open('MST_data/MST_2013.json', 'r', 'utf-8-sig'))
    incident_count = 0
    wounded_count = 0
    killed_count = 0
    for i in range(len(data)):
        incident_count = incident_count +1
        wounded_count = wounded_count + int(data[i]['wounded'])
        killed_count = killed_count + int(data[i]['killed'])
        print(int(data[i]['killed']),int(data[i]['wounded']))

    mapping_writer.writerow([2013, incident_count, wounded_count, killed_count])
    print(2013, incident_count, wounded_count, killed_count)

    data=json.load(codecs.open('MST_data/MST_2014.json', 'r', 'utf-8-sig'))
    incident_count = 0
    wounded_count = 0
    killed_count = 0
    for i in range(len(data)):
        incident_count = incident_count +1
        wounded_count = wounded_count + int(data[i]['wounded'])
        killed_count = killed_count + int(data[i]['killed'])
        print(int(data[i]['killed']),int(data[i]['wounded']))

    mapping_writer.writerow([2014, incident_count, wounded_count, killed_count])
    print(2014, incident_count, wounded_count, killed_count)

    data=json.load(codecs.open('MST_data/MST_2015.json', 'r', 'utf-8-sig'))
    incident_count = 0
    wounded_count = 0
    killed_count = 0
    for i in range(len(data)):
        incident_count = incident_count +1
        wounded_count = wounded_count + int(data[i]['wounded'])
        killed_count = killed_count + int(data[i]['killed'])
        print(int(data[i]['killed']),int(data[i]['wounded']))

    mapping_writer.writerow([2015, incident_count, wounded_count, killed_count])
    print(2015, incident_count, wounded_count, killed_count)
    
    data=json.load(codecs.open('MST_data/MST_2016.json', 'r', 'utf-8-sig'))
    incident_count = 0
    wounded_count = 0
    killed_count = 0
    for i in range(len(data)):
        incident_count = incident_count +1
        wounded_count = wounded_count + int(data[i]['wounded'])
        killed_count = killed_count + int(data[i]['killed'])
        print(int(data[i]['killed']),int(data[i]['wounded']))

    mapping_writer.writerow([2016, incident_count, wounded_count, killed_count])
    print(2016, incident_count, wounded_count, killed_count)

    data=json.load(codecs.open('MST_data/MST_2017.json', 'r', 'utf-8-sig'))
    incident_count = 0
    wounded_count = 0
    killed_count = 0
    for i in range(len(data)):
        incident_count = incident_count +1
        wounded_count = wounded_count + int(data[i]['wounded'])
        killed_count = killed_count + int(data[i]['killed'])
        print(int(data[i]['killed']),int(data[i]['wounded']))

    mapping_writer.writerow([2017, incident_count, wounded_count, killed_count])
    print(2017, incident_count, wounded_count, killed_count)

    data=json.load(codecs.open('MST_data/MST_2018.json', 'r', 'utf-8-sig'))
    incident_count = 0
    wounded_count = 0
    killed_count = 0
    for i in range(len(data)):
        incident_count = incident_count +1
        wounded_count = wounded_count + int(data[i]['wounded'])
        killed_count = killed_count + int(data[i]['killed'])
        print(int(data[i]['killed']),int(data[i]['wounded']))

    mapping_writer.writerow([2018, incident_count, wounded_count, killed_count])
    print(2018, incident_count, wounded_count, killed_count)

    data=json.load(codecs.open('MST_data/MST_2019.json', 'r', 'utf-8-sig'))
    incident_count = 0
    wounded_count = 0
    killed_count = 0
    for i in range(len(data)):
        incident_count = incident_count +1
        wounded_count = wounded_count + int(data[i]['wounded'])
        killed_count = killed_count + int(data[i]['killed'])
        print(int(data[i]['killed']),int(data[i]['wounded']))

    mapping_writer.writerow([2019, incident_count, wounded_count, killed_count])
    print(2019, incident_count, wounded_count, killed_count)

    data=json.load(codecs.open('MST_data/MST_2020.json', 'r', 'utf-8-sig'))
    incident_count = 0
    wounded_count = 0
    killed_count = 0
    for i in range(len(data)):
        incident_count = incident_count +1
        wounded_count = wounded_count + int(data[i]['wounded'])
        killed_count = killed_count + int(data[i]['killed'])
        print(int(data[i]['killed']),int(data[i]['wounded']))

    mapping_writer.writerow([2020, incident_count, wounded_count, killed_count])
    print(2020, incident_count, wounded_count, killed_count)

    data=json.load(codecs.open('MST_data/MST_2021.json', 'r', 'utf-8-sig'))
    incident_count = 0
    wounded_count = 0
    killed_count = 0
    for i in range(len(data)):
        incident_count = incident_count +1
        wounded_count = wounded_count + int(data[i]['wounded'])
        killed_count = killed_count + int(data[i]['killed'])
        print(int(data[i]['killed']),int(data[i]['wounded']))

    mapping_writer.writerow([2021, incident_count, wounded_count, killed_count])
    print(2021, incident_count, wounded_count, killed_count)

    data=json.load(codecs.open('MST_data/MST_2022.json', 'r', 'utf-8-sig'))
    incident_count = 0
    wounded_count = 0
    killed_count = 0
    for i in range(len(data)):
        incident_count = incident_count +1
        wounded_count = wounded_count + int(data[i]['wounded'])
        killed_count = killed_count + int(data[i]['killed'])
        print(int(data[i]['killed']),int(data[i]['wounded']))

    mapping_writer.writerow([2022, incident_count, wounded_count, killed_count])
    print(2022, incident_count, wounded_count, killed_count)


##################################################


df = pd.read_csv('Stanford_MSA_Database.csv')

df.drop_duplicates().to_csv('Stanford_MSA_Database_no_dups.csv', index=False)



years = ["1966", "1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990", "1991","1992", "1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014", "2015", "2016"]

with open('Stanford_MSA_Database_final.csv', mode='w') as syncHR:
    mapping_writer = csv.writer(syncHR, delimiter=',')

    mapping_writer.writerow(["Year", "Number_of_incidents", "Wounded", "Killed"])

    
    for year in years:
        incident_count = 0
        wounded_count = 0
        killed_count = 0
        with open('Stanford_MSA_Database_no_dups.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print( row[14][len(row[14])-4:len(row[14])],year )
                if(row[14][len(row[14])-4:len(row[14])]) == year:
                    incident_count = incident_count + 1
                    wounded_count = wounded_count + (int(row[12]) - int(row[11]))
                    killed_count = killed_count + int(row[11])
                    
            
        mapping_writer.writerow([year, incident_count, wounded_count, killed_count])
        print(year, incident_count, wounded_count, killed_count)

##################################################

print("Washington post")
df = pd.read_csv('WashingtonPost.csv')

df.drop_duplicates().to_csv('WashingtonPost_no_dups.csv', index=False)



years = ["1966", "1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990", "1991","1992", "1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]

with open('WashingtonPost_final.csv', mode='w') as syncHR:
    mapping_writer = csv.writer(syncHR, delimiter=',')

    mapping_writer.writerow(["Year", "Number_of_incidents", "Wounded", "Killed"])

    
    for year in years:
        incident_count = 0
        wounded_count = 0
        killed_count = 0
        with open('WashingtonPost_no_dups.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                
                if((row[2][len(row[2])-4:len(row[2])]) == year) and (row[11]=="1"):
                    print( row[2][len(row[2])-4:len(row[2])],year, row[11] )
                    incident_count = incident_count + 1
                    wounded_count = wounded_count + int(row[4])
                    killed_count = killed_count + int(row[3])
                    
            
        mapping_writer.writerow([year, incident_count, wounded_count, killed_count])
        print(year, incident_count, wounded_count, killed_count)