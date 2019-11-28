import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))

budget_csv = os.path.join("..","Resources","budget_data.csv")
output_csv = os.path.join("..","Output","budget_output.cvs")

print("Financial Analysis")
print("-------------------------")

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    month=0
    total = 0
    greatest_increase=0
    greatest_decrease=0
    for row in csvreader:
        month=month+1
        total=total+int(row[1])
        if int(row[1]) > greatest_increase:
            greatest_increase=int(row[1])
            greatest_increase_month=row[0]
        if int(row[1])<greatest_decrease:
            greatest_decrease=int(row[1])
            greatest_decrease_month=row[0]
    avg=round(total/month,2)

    print(f"Total months : {month}")
    print(f"Total: ${total}")
    print(f"Average Change: ${avg}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

with open(output_csv, 'w', newline='') as csvfile2:
    
    csvwriter = csv.writer(csvfile2, delimiter=',')
    csvwriter.writerow(['Total Months','Total', 'Average Change', 'Greatest Increase', 'Greatest Decrease'])
    csvwriter.writerow([month,total,avg,greatest_increase,greatest_decrease])