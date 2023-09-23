import csv

budget = "Resources/budget_data.csv"
analysis = "Analysis/analysis_results.txt"

Total_months = 0
Total_profit = 0
Total_change = 0
Change_count = 0
Greatest_increase = 0
Greatest_increase_month = ""
Greatest_decrease = 0
Greatest_decrease_month = ""


with open(budget) as budget_file:
    reader = csv.reader(budget_file)
    header = next (reader)
    
    Jan_row = next(reader)
    Total_months = Total_months + 1
    Total_profit = Total_profit + int(Jan_row[1])
    previous_profit = int(Jan_row[1])

    for row in reader:
        Total_months += 1    
        Total_profit += int(row[1])

        change = int(row[1]) - previous_profit
        Total_change += change
        Change_count += 1

        previous_profit = int(row[1])

        if change > Greatest_increase:
            Greatest_increase = change
            Greatest_increase_month = row[0]
        if change < Greatest_decrease:
            Greatest_decrease = change
            Greatest_decrease_month = row[0]
    
print(Greatest_decrease)    

output = f"""
Financial Analysis
----------------------------
Total Months: {Total_months}
Total: ${Total_profit:,}
Average Change: ${Total_change/Change_count:.2f}
Greatest Increase in Profits: Aug-16 (${Greatest_increase})
Greatest Decrease in Profits: Feb-14 (${Greatest_decrease})
"""

print(output)

with open(analysis, "w") as text_file:
    text_file.write(output)