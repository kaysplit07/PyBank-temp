import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")
# Define the function and have it accept the 'wrestlerData' as its sole parameter



# Read in the CSV file
with open(budget_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader=csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    month_count = 0
    net_amount = 0

    max_profit = 0
    max_profit_date =""

    max_loss = 0
    max_loss_date = ""

    # Loop through the data
    for row in csvreader:
        #print(row[1])
        month_count = month_count + 1
        net_amount = net_amount + int(row[1])

        if int(row[1]) > max_profit:
            max_profit = int(row[1])
            max_profit_date = row[0]
            #print(max_profit)
        
        if int(row[1]) < max_loss:
            max_loss = int(row[1])
            max_loss_date = row[0]
            #print(max_loss)


    average_change = round(net_amount/month_count,2)

L1 = "Financial Analysis"
L2 = "----------------------------"
L3 = f"Total Months: {month_count}"
L4 = f"Total: ${net_amount}"
L5 = f"Average Change: ${average_change}"
L6 = f"Greatest Increase in Profits: {max_profit_date} (${max_profit_date})"
L7 = f"Greatest Decrease in Profits: {max_loss_date} (${max_loss_date})"

print(f"{L1}\n{L2}\n{L3}\n{L4}\n{L5}\n{L6}\n{L7}")

    
file1 = open("OutputFile.txt", "w")

print_list = [L1, L2, L3, L4, L5, L6, L7]
[file1.writelines(f"{L}\n") for L in print_list]
file1.close()
