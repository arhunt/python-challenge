    # activate csv and os for file and csv pull
import os
import csv

    # Define the csv path
csvpath = os.path.join('Resources', 'election_data.csv')

    # Define initial variables
votes_counted = 0
votes = {}
percentage = {}
pcnt_cmp = []
compare = {}
winner = "Cacareco" # https://en.wikipedia.org/wiki/Cacareco

    # Call the CSV and isolate the header row
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
            # Count the number of votes
        votes_counted = votes_counted + 1
        row.append(votes_counted)

            # Is the candidate already on the tally?
        if row[2] not in votes:
                # No, add them in with one vote
            votes[row[2]] = 1
        else:
                # Yes, add one to their vote count
            votes[row[2]] += 1

    # Once all the calculations are done, figure percentages
for candidate in votes:
        # Matching the rounded decimals
    percent_vote = "{:.3%}".format(votes[candidate] / votes_counted)
        # Add the candidate's percentage to be able to reference
    percentage[candidate] = percent_vote
        # Add the percentage to be able to figure the maximum
            # This could do with votes too but already figuring percentages
    pcnt_cmp.append(percent_vote)
    compare[percent_vote] = candidate

    # Use the max pcnt_cmp to look up the candidate in the compare dictionary
winner = compare[max(pcnt_cmp)]

    # Print the results to the terminal
print("")
print("Election Results")
print("-------------------------")
print(f"Total votes: {votes_counted}")
print("-------------------------")
for candidate in votes:
    print(f"{candidate}: {percentage[candidate]} ({votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

    # Provide the text file path
txtpath = os.path.join('analysis', 'analysis.txt')

    # Write to the text file
with open(txtpath, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total votes: {votes_counted}\n")
    txtfile.write("-------------------------\n")
    for candidate in votes:
        txtfile.write(f"{candidate}: {percentage[candidate]} ({votes[candidate]})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
