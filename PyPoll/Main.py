#Import modules needed for working with CSV files
import os
import csv

#Create lists for data
voter_id = []
county = []
candidate = []

#Set path for raw data
pypollpath = os.path.join('resources', 'election_data.csv')

#Read CSV raw data file, exclude header row and put data in lists
with open(pypollpath, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    pypollheader = next(reader)
    for row in reader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#Determine number of votes overall, for each candidate and percentage won for each candidate 
totalvotes = len(voter_id)
candidatevotes = [(person,candidate.count(person),(candidate.count(person)/totalvotes)*100) for person in set(candidate)]

#Determine winner of election based on popular vote
winner = max(candidatevotes, key=lambda x: x[1])

#Set path for election results output
outpypollpath = os.path.join('resources', 'election_results.csv')

#Create CSV file containing election results output
with open(outpypollpath, 'w', newline='') as outfile:
    csvwrite =csv.writer(outfile, delimiter=',')
    csvwrite.writerow(['Total Votes', totalvotes, ''])
    for row in candidatevotes:
        csvwrite.writerow(row)
    csvwrite.writerow(['Winner', winner[0], ''])

#Print election results to terminal
print('')
print('Election Results')
print('----------------------------------------------------')
print(f'Total Votes: {totalvotes}')
print('----------------------------------------------------')
print(f'{candidatevotes[0][0]}: {candidatevotes[0][2]:.3f}% ({candidatevotes[0][1]})')
print(f'{candidatevotes[1][0]}: {candidatevotes[1][2]:.3f}% ({candidatevotes[1][1]})')
print(f'{candidatevotes[2][0]}: {candidatevotes[2][2]:.3f}% ({candidatevotes[2][1]})')
print(f'{candidatevotes[3][0]}: {candidatevotes[3][2]:.3f}% ({candidatevotes[3][1]})')
print('----------------------------------------------------')
print(f'Winner: {winner[0]}')
print('----------------------------------------------------')