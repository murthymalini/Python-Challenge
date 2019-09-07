import os
# Import CSV module
import csv
# Direct to CSV path with raw data
csv_path= os.path.join('budget_data.csv')

# create empty lists to iterate through specific rows
totalMonths = []
totalPL = []
monthlyPLChange = []

# open CSV file
with open(csv_path, 'r', newline='') as csvfile:    # make CSV reader
    pyBankReader = csv.reader(csvfile, delimiter=',')
    # skip header
    header = next(pyBankReader)
    # iterrate through all rows
    for row in pyBankReader:
        # populate lists
        totalMonths.append(row[0])
        totalPL.append(int(row[1])) 
        # count total rows
    for i in range(len(totalPL)-1):
        # find difference between two months and add to monthly PL change
        monthlyPLChange.append(totalPL[i+1]-totalPL[i])
        # get greatest increase in profits
        maxGain = max(monthlyPLChange)
        # get greatest decrease in losses
        maxLoss = min(monthlyPLChange)
        #associate correct month with min/max
        maxGainMonth = monthlyPLChange.index(max(monthlyPLChange))+1
        maxLossMonth = monthlyPLChange.index(min(monthlyPLChange))+1
    # print headers
    print("Financial Analysis\n--------------------------------------------------")
    # print total months
    print(f"The total number of months is:  {len(totalMonths)}")
    # print total profit loss
    print(f"The total profit/loss is {'${:,.2f}'.format(sum(totalPL))}")
    # print average g/l
    print(f"The average monthly profit/loss is: {'${:,.2f}'.format(round(sum(monthlyPLChange)/len(monthlyPLChange),2))}")
    # print max increase in profits
    print(f"Greatest Increase in Profits: {totalMonths[maxGainMonth]} {str('${:,.2f}'.format(maxGain))}")
    # print max losses in losses
    print(f"Greatest Decrease in Profits: {totalMonths[maxLossMonth]} {str('${:,.2f}'.format(maxLoss))}")

    # Output files
textFile = os.path.join("pyBankSummary.txt")

with open(textFile,"w") as file:
    
    # send output to text file
    file.write("Financial Analysis\n--------------------------------------------------\n")
    # print total months
    file.write(f"The total number of months is:  {len(totalMonths)}\n")
    # print total profit loss
    file.write(f"The total profit/loss is {str('${:,.2f}'.format(sum(totalPL)))}\n")
    # print average g/l
    file.write(f"The average monthly profit/loss is: {str('${:,.2f}'.format(round(sum(monthlyPLChange))/(len(monthlyPLChange))))}\n")
    # print max increase in profits
    file.write(f"Greatest Increase in Profits: {totalMonths[maxGainMonth]} {str('${:,.2f}'.format(maxGain))}\n")
    # print max losses in losses
    file.write(f"Greatest Decrease in Profits: {totalMonths[maxLossMonth]} {str('${:,.2f}'.format(maxLoss))}")