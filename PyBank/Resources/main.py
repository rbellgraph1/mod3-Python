import os 
import csv

# set path to csv 
file_to_load = os.path.join("..", "Resources", "budget_data.csv")
file_to_output = os.path.join("..","Resources", "budget_analysis.txt")

# set up the information that is needed to verify in a list 0 first and one second

total_months = 0 
months_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999]
total_net = 0 

# read the csv and convert to a list of dictionaries 

with open(file_to_load) as budget_analysis:
    reader = csv.reader(budget_analysis)

    #read the header row 
    header = next(reader)

    #extract first row to avoid appending to the next_change_list 
    first_row = next(reader)
    total_months += 1 
    total_net += int(first_row[1])
    prev_net = int(first_row[1])
#for loop to to loop though and gather the start and finish file to calculate from 
    for row in reader:

        #total amount of p&L 
        total_months += 1 
        total_net += int(row[1])

        #track the net change and if to get max and min 
        net_change = int(row[1]) - prev_net
        prev_net = int (row[1]) 
        net_change_list += [net_change]
        months_of_change += [row[0]]
        if net_change < greatest_decrease[1]: 
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
        if net_change > greatest_increase[1]: 
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
              

 #average change
net_change_sum = sum(net_change_list)
net_months_sum = len(months_of_change)
average = "{:.2f}".format(net_change_sum/net_months_sum)
  
   
#print the outcome 

print(f"Finanancial Analysis")
print("----------------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_net)}")
print(f"Average Change:  ${str(average)}")
print(f"Greatest Increase in Profits:  {str(greatest_increase [0])} ${str(greatest_increase[1])}")
print(f"Greatest Decrease in Profits:  {str(greatest_decrease [0])} ${str(greatest_decrease [1])}")


with open(file_to_output, "w") as txt_file:
    Summary_of_budget=(
    f"Finanancial Analysis\n"
    "----------------------------------\n"
    f"Total Months: {str(total_months)}\n"
    f"Total: ${str(total_net)}\n"
    f"Average Change:  ${str(average)}\n"
    f"Greatest Increase in Profits:  {str(greatest_increase [0])} ${str(greatest_increase[1])}\n"
    f"Greatest Decrease in Profits:  {str(greatest_decrease [0])} ${str(greatest_decrease [1])}\n"
    )
    # print(Summary_of_budget, end="")
    txt_file.write(Summary_of_budget)



# 	• The total number of months included in the dataset
# 	• The net total amount of "Profit/Losses" over the entire period
# 	• The changes in "Profit/Losses" over the entire period, and then the average of those changes
# 	• The greatest increase in profits (date and amount) over the entire period
# 	• The greatest decrease in profits (date and amount) over the entire period
# Your analysis should look similar to the following:

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
