import csv

Election = "Resources/election_data.csv"
Election_analysis = "Analysis/Election_results.txt"

output = f"""
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
"""

print(output)

with open(Election_analysis, "w") as text_file:
    text_file.write(output)