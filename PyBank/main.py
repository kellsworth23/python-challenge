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
print("```text")
print("Financial Analysys")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${'{:.2f}'.format(average_change)}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

with open("./analysis/budget_analysis.csv", "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["```text"])
    writer.writerow(["Financial Analysys"])
    writer.writerow(["----------------------------"])
    writer.writerow(["Total Months: " + str(total_months)])
    writer.writerow(["Total: $" + str(total_profit_losses)])
    writer.writerow(["Average Change: $" + '{:.2f}'.format(average_change)])
    writer.writerow(["Greatest Increase in Profits: " + greatest_increase[0] + " ($" + str(greatest_increase[1]) + ")"])
    writer.writerow(["Greatest Decrease in Profits: " + greatest_decrease[0] + " ($" + str(greatest_decrease[1]) + ")"])