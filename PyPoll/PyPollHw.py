# import dependencies
import os
import csv
# direct to CSV file
electionCSV = os.path.join('election_data.csv')

# create empty dictionary to iterate through rows
result={}
totalVotes = 0

# open csv
with open(electionCSV,'r', newline='', encoding="UTF-8") as csvfile:
    pyPollReader = csv.reader(csvfile, delimiter=',')
    #skip header
    header = next(pyPollReader)
    #iterate through all rows
    for row in pyPollReader:
        totalVotes +=1
        if row[2] not in result:
            result[row[2]]=1
        else:
            result[row[2]]+=1
# generate list of unique candidates, candidates are the key in the dictionary
candVotes = list(result.keys())
# calculate total number votes for each unique candidate, the value is the vote count
resultVotes = list(result.values())
# test print values
# print(resultVotes)
# print(candVotes)
# print headers

# print(f"Total Votes Places is: {'{:,.0f}'.format(totalVotes)}")
# print(result)
print(f"Election Results\n----------------------------------------\nTotal Votes: {'{:,.0f}'.format(totalVotes)}\n----------------------------------------")
# math works in the % calculation because of PEMDAS
print(f"{candVotes[0]}: {'{:,.0f}'.format(resultVotes[0]/totalVotes*100)}% ({'{:,.0f}'.format(resultVotes[0])})")
print(f"{candVotes[1]}: {'{:,.0f}'.format(resultVotes[1]/totalVotes*100)}% ({'{:,.0f}'.format(resultVotes[1])})")
print(f"{candVotes[2]}: {'{:,.0f}'.format(resultVotes[2]/totalVotes*100)}% ({'{:,.0f}'.format(resultVotes[2])})")
print(f"{candVotes[3]}: {'{:,.0f}'.format(resultVotes[3]/totalVotes*100)}% ({'{:,.0f}'.format(resultVotes[3])})")
print("----------------------------------------")
print(f"Winner: {candVotes[0]}")
print("----------------------------------------")

 # Output files
textFile = os.path.join("pyPollSummary.txt")

with open(textFile,"w") as file:
    # send output to text file
    file.write(f"Election Results\n----------------------------------------\nTotal Votes: {'{:,.0f}'.format(totalVotes)}\n----------------------------------------\n")
    file.write(f"{candVotes[0]}: {'{:,.0f}'.format(resultVotes[0]/totalVotes*100)}% ({'{:,.0f}'.format(resultVotes[0])})\n")
    file.write(f"{candVotes[1]}: {'{:,.0f}'.format(resultVotes[1]/totalVotes*100)}% ({'{:,.0f}'.format(resultVotes[1])})\n")
    file.write(f"{candVotes[2]}: {'{:,.0f}'.format(resultVotes[2]/totalVotes*100)}% ({'{:,.0f}'.format(resultVotes[2])})\n")
    file.write(f"{candVotes[3]}: {'{:,.0f}'.format(resultVotes[3]/totalVotes*100)}% ({'{:,.0f}'.format(resultVotes[3])})\n")
    file.write(f"----------------------------------------\n")
    file.write(f"Winner: {candVotes[0]}\n")
    file.write("----------------------------------------")