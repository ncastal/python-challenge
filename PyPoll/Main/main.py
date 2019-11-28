import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
election_csv = os.path.join("..","Resources","election_data.csv")

print("Election Results")
print("-------------------------")

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    total_votes=0
    khan_votes=0
    correy_votes=0
    li_votes=0
    otooley_votes=0
    for row in csvreader:
        total_votes=total_votes+1
        if row[2]=="Khan":
            khan_votes=khan_votes+1
        if row[2]=="Correy":
            correy_votes=correy_votes+1
        if row[2]=="Li":
            li_votes=li_votes+1
        if row[2]=="O'Tooley":
            otooley_votes=otooley_votes+1  
    canidates={"Khan":khan_votes,"Correy":correy_votes,"Li":li_votes,"O'Tooley":otooley_votes}
    
    percent_khan = round((khan_votes/total_votes)*100,2)
    percent_correy = round((correy_votes/total_votes)*100,2)
    percent_li = round((li_votes/total_votes)*100,2)
    percent_otooley=round((otooley_votes/total_votes)*100,2)
    print(f"Total votes: {total_votes}")
    print("-------------------------")
    print(f"Khan: {percent_khan}% ({khan_votes})")
    print(f"Correy: {percent_correy}% ({correy_votes})")
    print(f"Li: {percent_li}% ({li_votes})")
    print(f"O'Tooley: {percent_otooley}% ({otooley_votes})")
    print("-------------------------")
    winner = max(canidates, key=canidates.get)
    print(f"Winner: {winner}")
    print("-------------------------")