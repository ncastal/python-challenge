import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))

budget_csv = os.path.join("..","Resources","budget_data.csv")

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    print(len(csvfile))