import os
import csv

# Path to collect data

poldata_csv = os.path.join('/Users/bwalsh/Documents/UCB-BER-DATA-PT-08-2019-U-C/homework/03-Python/Instructions/PyPoll/Resources/election_data.csv')

# Set variables

total_votes = 0
canditate = ''
candidate_list = []
vote_list = []
percent_list = []
winner = ''

#open CSV file

with open(poldata_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Total votes and list of candidates

    for row in csvreader:
        total_votes += 1

        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            vote_list.append(1)
        else: 
            vote_list[candidate_list.index(row[2])] += 1

# List vote percentages for each candidate

percent_list = [(100 / total_votes) * i for i in vote_list]

# Produce winner

winner = candidate_list[vote_list.index(max(vote_list))]

# Print out results

print(f"Election Results")
print(f"--------------------")
print(f"Total Votes: {total_votes}")
print(f"--------------------")

for i in candidate_list:
    print(i + ": " + str(format(percent_list[candidate_list.index(i)], '.2f')) 
        + "% (" + str(vote_list[candidate_list.index(i)]) + ")")


print(f"--------------------")
print(f"Winner: {winner}")
print(f"--------------------")






