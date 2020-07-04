    # activate csv and os for file and csv pull
import os
import csv

    # Define the csv path
csvpath = os.path.join('Resources', 'election_data.csv')

    # Define initial variables
votes_counted = 0
    # List the candidate to votes received
votes = {}
    # List the candidate to percentage of votes
percentage = {}
    # Name of the winner
winner = []

    # Call the CSV and isolate the header row
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

        # Processing each row as a vote
    for row in csvreader:
            # Count the number of votes
        votes_counted = votes_counted + 1
            # Is the candidate already on the tally?
        if row[2] not in votes:
                # No, add them in with one vote
            votes[row[2]] = 1
        else:
                # Yes, add one to their vote count
            votes[row[2]] += 1

    # Create a list with the final vote values
vote_values = list(votes.values())

    # Once all the calculations are done, figure percentages
for candidate in votes:
        # Matching the rounded decimals in the example
    percent_vote = "{:.3%}".format(votes[candidate] / votes_counted)
        # Add the candidate's percentage to be able to reference
    percentage[candidate] = percent_vote
        # Match the name to the max of the final vote values
    if votes[candidate] == max(vote_values):
        winner.append(candidate)

    # Print the results to the terminal
print("")
print("Election Results")
print("-------------------------")
print(f"Total votes: {votes_counted}")
print("-------------------------")
for candidate in votes:
    print(f"{candidate}: {percentage[candidate]} ({votes[candidate]})")
print("-------------------------")
    # Determine a single winner or a tie
if len(winner) == 1:
    for candidate in winner:
        print(f"Winner: {candidate}")
else:
    print("Winner: Tie between:")
    for candidate in winner:
        print(f"{candidate}")

print("-------------------------")
print("")

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

    if len(winner) == 1:
        for candidate in winner:
            txtfile.write(f"Winner: {candidate}\n")
    else:
        txtfile.write("Winner: Tie between:\n")
        for candidate in winner:
            txtfile.write(f"{candidate}\n")

    txtfile.write("-------------------------\n")
