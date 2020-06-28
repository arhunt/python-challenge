    # activate csv and os for file and csv pull
import os
import csv

    # Define the csv path
csvpath = os.path.join('Resources', 'budget_data.csv')

    # Define initial variables
net_total_profit = 0
last_profit = 0
profit_difference = []
# month = []
# profit = []
count_months = 0

    # Call the CSV and isolate the header row
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
   
    for row in csvreader:
            # Count how many rows there are
        count_months = count_months + 1
        # month.append(row[0])
        # profit.append(row[1])
            # Add the profit value to the running total
        net_total_profit = net_total_profit + int(row[1])
            # Calculate the change in profit from previous row
        profit_change = (int(row[1]) - last_profit)
            # Add this value to the profit difference list
        profit_difference.append(profit_change)

            # Determine whether this month's change is the new max/min
            # Store the change and month name if it is
        if profit_change == max(profit_difference):
            max_incr = profit_change
            max_incr_mth = row[0]
        if profit_change == min(profit_difference):
            max_decr = profit_change
            max_decr_mth = row[0]
        
            # Set this month's profit as next month's last profit
        last_profit = int(row[1])

    # with the profit_difference list complete find the average
average_change = round ( sum(profit_difference) / count_months , 2)

    # Print the results in the terminal
print("")
print("Financial Analysis")
print("------------------------------------------------------")
print(f"Total Months: {count_months}")    
print(f"Total: ${net_total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_incr_mth} with ${max_incr}")
print(f"Greatest Decrease in Profits: {max_decr_mth} with ${max_decr}")
print("------------------------------------------------------")

    # Provide the text file path
txtpath = os.path.join('analysis', 'analysis.txt')

    # Write to the text file
with open(txtpath, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------------------------------------------\n")
    txtfile.write(f"Total Months: {count_months}\n")   
    txtfile.write(f"Total: ${net_total_profit}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {max_incr_mth} with ${max_incr}\n")
    txtfile.write(f"Greatest Decrease in Profits: {max_decr_mth} with ${max_decr}\n")
    txtfile.write("------------------------------------------------------\n")
