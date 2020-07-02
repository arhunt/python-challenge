    # activate csv and os for file and csv pull
import os
import csv

    # Define the csv path
csvpath = os.path.join('Resources', 'budget_data.csv')

    # Define initial variables
net_total_profit = 0
last_profit = 0
profit_difference = []
count_months = 0

    # Call the CSV and isolate the header row
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
   
    for row in csvreader:
            # Count how many rows there are
        count_months = count_months + 1
        row.append(count_months)
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

            # Keep track of the first and final profit values        
        if row[2] == 1:
            first_profit = int(row[1])
        if row[2] == count_months:
            final_profit = int(row[1])
        
            # Set this month's profit as next month's last profit
        last_profit = int(row[1])

    # with the profit_difference list complete find the average
average_change = round ( (final_profit - first_profit) / (count_months - 1) , 2)

    # Print the results in the terminal
print("")
print("Financial Analysis")
print("---------------------------------------------------")
print(f"Total Months: {count_months}")    
print(f"Total: ${net_total_profit}")
print(f"Average Change: ${average_change}")
if max_incr < 0:
    print(f"Greatest Increase in Profits: ${max_incr} ({max_incr_mth})")
else:
    print(f"Greatest Increase in Profits: $ {max_incr} ({max_incr_mth})")
if max_decr < 0:
    print(f"Greatest Decrease in Profits: ${max_decr} ({max_decr_mth})")
else:
    print(f"Greatest Decrease in Profits: $ {max_decr} ({max_decr_mth})")
print("---------------------------------------------------")

    # Provide the text file path
txtpath = os.path.join('analysis', 'analysis.txt')

    # Write to the text file
with open(txtpath, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------------------------------------\n")
    txtfile.write(f"Total Months: {count_months}\n")   
    txtfile.write(f"Total: ${net_total_profit}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    if max_incr < 0:
        txtfile.write(f"Greatest Increase in Profits: ${max_incr} ({max_incr_mth})\n")
    else:
        txtfile.write(f"Greatest Increase in Profits: $ {max_incr} ({max_incr_mth})\n")
    if max_decr < 0:
        txtfile.write(f"Greatest Decrease in Profits: ${max_decr} ({max_decr_mth})\n")
    else:
        txtfile.write(f"Greatest Decrease in Profits: $ {max_decr} ({max_decr_mth})\n")
    txtfile.write("---------------------------------------------------\n")
