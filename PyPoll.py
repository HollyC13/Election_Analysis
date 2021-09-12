# Data we need to retrieve.
# 1.  Total number of votes cast
# 2.  Complete list of candidates who received votes
# 3.  Percentage of votes each candidate won
# 4.  Total number of votes each candidate won
# 5.  Winner of the election based on popular vote

# Import dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1.  Initialize a vote counter
total_votes = 0

# Declare list for candidate options
candidate_options = []

# Declare dictionary for candidate votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
# Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read header row
    headers = next(file_reader)
 
    # Print each row in the CSV file
    for row in file_reader:
        # 2.  Add to the total vote count
        total_votes += 1
        
        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add it to the candidate_options list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's votes
            candidate_votes[candidate_name] = 0

        # Add a vote to candidate's vote count
        candidate_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------\n"
        f"Total Votes:  {total_votes:,}\n"
        f"-------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine percentage of votes by candidate by looping through vote counts
    #1.  Iterate through the candidate list
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # 3.  Calcualte percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print out each candidate's name, vote count, and percentage
        # of votes to the terminal.
        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #Determine winning vote count and candidate
        #Determine if the vote count is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percentage = 
            # vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's
            # name.
            winning_candidate = candidate_name

        
    # Print out the winning candidate, vote count and percentage
    # to terminal.
    winning_candidate_summary = (
        f"-------------------------------------\n"
        f"Winner:  {winning_candidate}\n"
        f"Winning Vote Count:  {winning_count:,}\n"
        f"Winning Percentage:  {winning_percentage:.1f}%\n"
        f"-------------------------------------\n")
    # print(winning_candidate_summary)
