import os
import csv

date = []
pl = []
change = [0]

pybankpath = os.path.join('Resources', 'budget_data.csv')

with open(pybankpath, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    pybankheader = next(reader)
    for row in reader:
        date.append(row[0])
        pl.append(int(row[1])) 

totalmonths = len(date)
totalprofit = sum(pl)

tchange = [x-y for x, y in zip(pl[1:], pl)]
avgchange = float('{0:.2f}'.format(sum(tchange)/len(tchange)))
change.extend(tchange)

pybankdata = zip(date, pl, change)
pybankdata = set(pybankdata)

maxchange = max(pybankdata, key=lambda x: x[2])
minchange = min(pybankdata, key=lambda x: x[2])

outpybankpath = os.path.join('Resources', 'financial _analysis.csv')

with open(outpybankpath, 'w', newline='') as outfile:
    csvwriter = csv.writer(outfile, delimiter=',')
    csvwriter.writerow(['Total Months', 'Total', 'Average Change', 'Greatest Increase Date', 'Greatest Increase', 'Greatest Decrease Date', 'Greatest Decrease'])
    csvwriter.writerow([totalmonths, totalprofit, avgchange, maxchange[0], maxchange[2], minchange[0], minchange[2]])

print('')
print('Financial Analysis')
print('----------------------------------------------------')
print(f'Total Months: {totalmonths}')
print(f'Total: {totalprofit}')
print(f'Average Change: {avgchange}')
print(f'Greatest Increase in Profits: {maxchange[0]} (${maxchange[2]})')
print(f'Greatest Decrease in Profits: {minchange[0]} (${minchange[2]})')
print('----------------------------------------------------')
