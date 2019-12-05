import os #import libraries
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__))) #change working directory to one where the python file is located

budget_csv = os.path.join("..","Resources","budget_data.csv") #giving the location for budget_data.csv
budget_txt= os.path.join("..","Output","budget_output.txt") #setting location for budget output text file

print("Financial Analysis")
print("-------------------------")

with open(budget_csv, newline="") as csvfile: #reading budget_data.csv
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile) #skipping header
    month=0 #variable to count how many months are in the csv file
    total = 0 #variable to give a sum of all profits and losses
    greatest_increase=0 #varaible used to find the greatest increase in profits
    greatest_decrease=0 #variable used to find the greatest decrease in profits
    for row in csvreader:
        month=month+1 #finding the total amount of months
        total=total+int(row[1]) #finding the sum of all profits and losses
        if int(row[1]) > greatest_increase: #if statements to find greatest increases and decreases
            greatest_increase=int(row[1])
            greatest_increase_month=row[0]
        if int(row[1])<greatest_decrease:
            greatest_decrease=int(row[1])
            greatest_decrease_month=row[0]
    avg=round(total/month,2) #calcuating the average and rounding it to two decimals

    print(f"Total months : {month}") #printing the results
    print(f"Total: ${total}")
    print(f"Average Change: ${avg}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

with open(budget_txt, 'w') as writer: #writing the info to a text file
    
    writer.write("Financial Analysis\n")
    writer.write("-------------------------\n")
    writer.write(f"Total months : {month}\n")
    writer.write(f"Total: ${total}\n")
    writer.write(f"Average Change: ${avg}\n")
    writer.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    writer.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")