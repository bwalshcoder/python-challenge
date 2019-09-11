import os
import csv

# Path to collect data

bankdata_csv = os.path.join('/Users/bwalsh/Documents/UCB-BER-DATA-PT-08-2019-U-C/homework/03-Python/Instructions/PyBank/Resources/budget_data.csv')

# Set Variables

total_months = 0
total_revenue = 0
monthly_change = []
month_count = []
biggest_profit = 0
biggest_profit_month = 0
biggest_loss = 0
biggest_loss_month = 0

# Open CSV file

with open(bankdata_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)
    row = next(csvreader)

    previous_row = int(row[1])
    total_months += 1
    total_revenue += int(row[1])
    biggest_profit += int(row[1])
    biggest_profit_month = row[0]

    # Calculate Total Months and Total Revenue

    for row in csvreader:
        total_months += 1
        total_revenue += int(row[1])

        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])

        # Calculate Biggest Profit and Loss

        if int(row[1]) > biggest_profit:
            biggest_profit = int(row[1])
            biggest_profit_month = row[0]

        if int(row[1]) < biggest_loss:
            biggest_loss = int(row[1])
            biggest_loss_month = row[0]

        # Average Change

        average_change = sum(monthly_change) / len(monthly_change)

        highest = max(monthly_change)
        lowest = min(monthly_change)

    # Print Results

    print(f"Financial Analysis:")
    print(f"------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Revenue: ${total_revenue}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Profit Increase:, {biggest_profit_month}, (${highest})")
    print(f"Greatet Profit Decrease:, {biggest_loss_month}, (${lowest})")

    # Write results to a text file

text_file = os.path.join('/Users/bwalsh/Desktop/LearnPython/python-challenge/PyBank/Budget_Analysis.text')

with open(text_file, 'w',) as text_file:
    text_file.write(f"Financial Analysis \n")
    text_file.write(f"------------------------------ \n")
    text_file.write(f"Total Months: {total_months} \n")
    text_file.write(f"Total Revenue: ${total_revenue} \n")
    text_file.write(f"Average Change: ${average_change:.2f} \n")
    text_file.write(f"Greatest Profit Increase:, {biggest_profit_month}, (${highest}) \n")
    text_file.write(f"Greatet Profit Decrease:, {biggest_loss_month}, (${lowest}) \n")


