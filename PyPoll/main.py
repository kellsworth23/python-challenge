import os
import csv

# Variables
# Total number of votes
total_votes = 0
# Candidates List with  candidate name, and total votes
candidates = {}
# Variables to determine the winner
winner_votes = 0
winner_name = ""

# function that prints out the results to terminal, and to file
def print_result(result):
    for item in result:
        print(item)
    # Export the results to text file
    with open("./analysis/election_analysis.txt", "w") as text_file:
        for item in result:
            text_file.write(item + '\n')


votes_csv = os.path.join(".", "Resources", "election_data.csv")
with open(votes_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        candidate = row[2]
        total_votes = total_votes + 1
        if candidate in candidates:
            candidates[candidate] = candidates[candidate] + 1
        else: 
            candidates[candidate] = 1

# Generating analysis
display = []
display.append("```text")
display.append("Election Results")
display.append("-------------------------")
display.append("Total Votes: " + str(total_votes))
display.append("-------------------------")
for key, value in candidates.items():
    if value > winner_votes:
      winner_name = key
      winner_votes = value
    votes_percentage = value*100/total_votes  
    print(str(votes_percentage))
    display.append(key + ": " + '{:.3f}'.format(votes_percentage) + "% (" + str(value) + ")")
display.append("-------------------------")
display.append("Winner: " + winner_name)
display.append("-------------------------")
display.append("```")  
  
# Print the analysis results to the console and to the file
print_result(display)