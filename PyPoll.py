#Data we need to retrieve.
# 1.  Total number of votes cast
# 2.  Complete list of candidates who received votes
# 3.  Percentage of votes each candidate won
# 4.  Total number of votes each candidate won
# 5.  Winner of the election based on popular vote

#Import dependencies
import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:
#Read the file object with the reader function
    file_reader = csv.reader(election_data)

#REad/Print header row
    headers = next(file_reader)
    print(headers)



#Print each row in the CSV file
    for row in file_reader:
        print(row[0])









    #Print the file object
    print(election_data)



#Using the open()function with the "w" mode we will write data to the file
open(file_to_save, "w")

#Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
    #Write data to file
    txt_file.write("Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")

