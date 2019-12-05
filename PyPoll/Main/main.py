import os #importing libraries
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__))) #change working directory to one where the python file is located
election_csv = os.path.join("..","Resources","election_data.csv") #giving the location for election_data.csv
election_result = os.path.join("..","Output","election_result.txt") #setting location for election result text file


print("Election Results")
print("-------------------------")

with open(election_csv, newline="") as csvfile: #reading election_data.csv
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile) #skipping header
    total_votes=0 #variable to count how many total votes
    khan_votes=0 #variables to count how many votes for each canidate
    correy_votes=0
    li_votes=0
    otooley_votes=0
    for row in csvreader: 
        total_votes=total_votes+1 #counting total votes
        if row[2]=="Khan": #If statements to count votes for each canidate
            khan_votes=khan_votes+1
        if row[2]=="Correy":
            correy_votes=correy_votes+1
        if row[2]=="Li":
            li_votes=li_votes+1
        if row[2]=="O'Tooley":
            otooley_votes=otooley_votes+1  
    canidates={"Khan":khan_votes,"Correy":correy_votes,"Li":li_votes,"O'Tooley":otooley_votes} #creating a dictonary for the canidates and votes cast for them
    
    percent_khan = round((khan_votes/total_votes)*100,2) #calculating the percentage of the votes each candiate recieved
    percent_correy = round((correy_votes/total_votes)*100,2)
    percent_li = round((li_votes/total_votes)*100,2)
    percent_otooley=round((otooley_votes/total_votes)*100,2)
    print(f"Total votes: {total_votes}") #printing the results
    print("-------------------------")
    print(f"Khan: {percent_khan}% ({khan_votes})")
    print(f"Correy: {percent_correy}% ({correy_votes})")
    print(f"Li: {percent_li}% ({li_votes})")
    print(f"O'Tooley: {percent_otooley}% ({otooley_votes})")
    print("-------------------------")
    winner = max(canidates, key=canidates.get) #determines the winner of election by finding the canidate with the most votes
    print(f"Winner: {winner}")
    print("-------------------------")

with open(election_result, 'w') as writer: #wtiting the results to a text file
    writer.writelines('Election Results\n')
    writer.writelines(f"Total votes: {total_votes}\n")
    writer.writelines("-------------------------\n")
    writer.writelines(f"Khan: {percent_khan}% ({khan_votes})\n")
    writer.writelines(f"Correy: {percent_correy}% ({correy_votes})\n")
    writer.writelines(f"Li: {percent_li}% ({li_votes})\n")
    writer.writelines(f"O'Tooley: {percent_otooley}% ({otooley_votes})\n")
    writer.writelines("-------------------------\n")
    writer.writelines(f"Winner: {winner}\n")
    writer.writelines("-------------------------\n")