import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))

budget_csv = os.path.join("..","Resources","budget_data.csv")

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    month=0
    for row in csvfile:
        month=month+1
    print(month)