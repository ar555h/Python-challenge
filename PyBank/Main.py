import os
import csv

#Set Variables
totalnumbermonths = 0
totalrevenue = 0
revenue = []
previousrevenue = 0
monthofchange = []
change = 0
decrease = ["", 9999999]
increase = ["", 0]
changelist = []
revenueaverage = 0

#Path to CSV File
budgetdatacsv = os.path.join ('/Users/SOSA/Documents/github/python-challenge/pybank/resources/budget_data.csv')

#Open CSV file
with open (budgetdatacsv, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
         
         #Total number of Months
         totalnumbermonths= totalnumbermonths + 1

         #Calculate to sum of revenue
         totalrevenue = totalrevenue + int(row["Profit/Losses"])

         #Calculate average change in revenue
         change = float(row["Profit/Losses"])- previousrevenue
         previousrevenue = float(row["Profit/Losses"])
         changelist = changelist + [change]
         monthofchange = [monthofchange] + [row["Date"]]

         #Largest increase in revenue
         if change>increase[1]:
            increase[1]= change
            increase[0] = row['Date']

         #Largest decrease in revenue
         if change<decrease[1]:
            decrease[1]= change
            decrease[0] = row['Date']
    revenueaverage = sum(changelist)/len(changelist)

#Print to terminal
print("Financial Analysis\n")
print("---------------------\n")
print("Total Months: %d\n" % totalnumbermonths)
print("Total Revenue: $%d\n" % totalrevenue)
print("Average Revenue Change $%d\n" % revenueaverage)
print("Greatest Increase in Revenue: %s ($%s)\n" % (increase[0], increase[1]))
print("Greatest Decrease in Revenue: %s ($%s)\n" % (decrease[0], decrease[1]))

#Set path to output file
text_path = ('/Users/SOSA/Documents/github/python-challenge/pybank/analysis/output.txt')

#Write txt file
with open(text_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % totalnumbermonths)
    file.write("Total Revenue: $%d\n" % totalrevenue)
    file.write("Average Revenue Change $%d\n" % revenueaverage)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (increase[0], increase[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (decrease[0], decrease[1]))

