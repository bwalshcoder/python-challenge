import os
import csv

# Path to collect data

bankdata_csv = os.path.join('/Users/bwalsh/Documents/UCB-BER-DATA-PT-08-2019-U-C/homework/03-Python/Instructions/PyBank/Resources/budget_data.csv')

with open(bankdata_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    #row = next(csvreader)
    total_months = 0
    month_count = []
    total_revenue = 0
    #previous_row = int(row[1])
    # Calculate total months and revenue
    
    for row in csvreader:
        total_months += 1
        total_revenue += int(row[1])
        #month_count.append(row[0])
    
    print(f"Financial Analysis:")
    print(f"------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Revenue: ${total_revenue}")





