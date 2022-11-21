# -*- coding: utf-8 -*-

import pprint
import csv

from datetime import datetime, timedelta


def f(x):
    return {
        0: "Mon",
        1: "Tue",
        2: "Wed",
        3: "Thu",
        4: "Fri",
        5: "Sat",
        6: "Sun",

    }[x]


with open('MotherJones.csv', mode='w') as syncHR:
    mapping_writer = csv.writer(syncHR, delimiter=',')
    # mapping_writer3.writerow(["Date", "Time (local)", "Team2_P01", "Team2_P02", "Team2_P03"])

    mapping_writer.writerow(["Year", "Number_of_incidents"])

    with open('MotherJones_original.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # i =0
        prev_year = 0
        for row in readCSV:
            if row[23]=="year":
                print(row[23])
            elif prev_year ==0:
                prev_year = row[23]
                count = 1
            elif prev_year==row[23]:
                count = count + 1
            else:
                mapping_writer.writerow([prev_year, count])
                prev_year = row[23]
                count = 1
            