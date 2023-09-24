import csv

Election = "Resources/election_data.csv"
Election_analysis = "Analysis/Election_results.txt"

Total_Votes = 0
Candidates = {}
winner = ""
winner_votes = 0

with open(Election) as Election_file:
    reader = csv.reader(Election_file)
    header = next (reader)    

    for row in reader:
        Total_Votes += 1
        candidate_name = row[2]

        if candidate_name in Candidates:
            Candidates[candidate_name] += 1
        else:
            Candidates[candidate_name] = 1
    #Calculations of percentage of votes each candidate won
for Candidates, votes in Candidates.items():
    if votes > winner_votes:
        winner_votes = votes
        winner = Candidates

print(winner)

output = f"""
Election Results
-------------------------
Total Votes: {Total_Votes}
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: {winner}
-------------------------
"""

print(output)

with open(Election_analysis, "w") as text_file:
    text_file.write(output)
