import os
import csv

# Variables
# Total number of months included in the dataset
total_months = 0
# Net total amount of profit/losses over the entire period
total_profit_losses = 0
# Changes in Profit/Losses over the entire period
total_change = 0
# current and last will help to determine the total changes
current = 0
last = 0
# Average of canges in Profit/Losses
average_change = 0

greatest_increase = ["", -9999999999]
greatest_decrease = ["", 9999999999]

# function that prints out the results to terminal, and to file
def print_result(result):
    for item in result:
        print(item)
    # Export the results to text file
    with open("./analysis/budget_analysis.txt", "w") as text_file:
        for item in result:
            text_file.write(item + '\n')


# Main
budget_csv = os.path.join(".", "Resources", "budget_data.csv")
with open(budget_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        total_months = total_months + 1
        total_profit_losses = total_profit_losses + int(row[1])
        current = int(row[1])
        if total_months > 1:
            change = current - last
            total_change = total_change + change
            if change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = change
            if change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = change
        last = int(row[1])

average_change = total_change / (total_months - 1) 

# Generating analysis
display = []
display.append("```text")
display.append("Financial Analysys")
display.append("----------------------------")
display.append("Total Months: " + str(total_months))
display.append("Total: $" + str(total_profit_losses))
display.append("Average Change: $" + '{:.2f}'.format(average_change))
display.append("Greatest Increase in Profits: " + greatest_increase[0] + " ($" + str(greatest_increase[1]) + ")")
display.append("Greatest Decrease in Profits: " + greatest_decrease[0] + " ($" + str(greatest_decrease[1]) + ")")
# Print the analysis results to the console and to the file
print_result(display)