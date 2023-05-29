import os
import csv
     
#Set Variables
totalnumbervotes = 0
can = []
votesper = {}
winnervotes = 0
winner = ""


#Path to CSV File
electiondatacsv = os.path.join ('/Users/SOSA/Documents/github/python-challenge/pypoll/resources/election_data.csv')

#Open CSV file
with open (electiondatacsv, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
         
         #The total number of votes cast
         totalnumbervotes= totalnumbervotes + 1

         #A complete list of candidates who received votes 
         if row["Candidate"] not in can:
              
              can.append(row["Candidate"])
              votesper[row["Candidate"]] = 1
              
         else:
              votesper [row["Candidate"]] = votesper[row["Candidate"]] + 1 

    #The winner of the election based on popular vote
    for row["Candidate"] in votesper:
              
              canvotes = votesper [row["Candidate"]]

              if (canvotes > winnervotes):

                winnervotes = canvotes

                winner = row["Candidate"]

candidate = row["Candidate"]

print("Election Results")
print("-------------------------")
print("Total Votes " + str(totalnumbervotes))
print("-------------------------")


     
percent = (canvotes / totalnumbervotes)*100

out = f"{candidate}: {percent}% {canvotes}"


print(out)


print ("Winner: " + winner)

