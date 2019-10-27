#Import modules needed for working with CSV files
import os
import csv

#Create lists for data
date = []
pl = []
change = [0]

#Set path for raw data
pybankpath = os.path.join('Resources', 'budget_data.csv')

#Read CSV raw data file, exclude header row and put data in lists
with open(pybankpath, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    pybankheader = next(reader)
    for row in reader:
        date.append(row[0])
        pl.append(int(row[1])) 

#Determine number of months involved in analysis and total profits
totalmonths = len(date)
totalprofit = sum(pl)

#Determine average monthly change in profits/losses and create monthly change list
tchange = [x-y for x, y in zip(pl[1:], pl)]
avgchange = float('{0:.2f}'.format(sum(tchange)/len(tchange)))
change.extend(tchange)

#Create list of date, profit/loss, change
pybankdata = zip(date, pl, change)
pybankdata = set(pybankdata)

#Determine the max and min change in profit/loss based on all months
maxchange = max(pybankdata, key=lambda x: x[2])
minchange = min(pybankdata, key=lambda x: x[2])

#Set path for financial analysis output
outpybankpath = os.path.join('Resources', 'financial _analysis.csv')

#Create CSV file containing financial analysis output
with open(outpybankpath, 'w', newline='') as outfile:
    csvwriter = csv.writer(outfile, delimiter=',')
    csvwriter.writerow(['Total Months', 'Total', 'Average Change', 'Greatest Increase Date', 'Greatest Increase', 'Greatest Decrease Date', 'Greatest Decrease'])
    csvwriter.writerow([totalmonths, totalprofit, avgchange, maxchange[0], maxchange[2], minchange[0], minchange[2]])

#Print financial analysis to terminal
print('')
print('Financial Analysis')
print('----------------------------------------------------')
print(f'Total Months: {totalmonths}')
print(f'Total: {totalprofit}')
print(f'Average Change: {avgchange}')
print(f'Greatest Increase in Profits: {maxchange[0]} (${maxchange[2]})')
print(f'Greatest Decrease in Profits: {minchange[0]} (${minchange[2]})')
print('----------------------------------------------------')
