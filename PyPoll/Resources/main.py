import os 
import csv

# # Path to collect data from the Resources folder
election_data =os.path.join('..', 'Resources', 'election_data.csv')
output_file = os.path.join('..', 'analysis', 'election_analysis.txt')

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

     #read the header row 
    csvheaders = next(csvreader)

    total_votes = 0
    # Ballot_id = []
    # County = []
    Candidate_Options =[]
    # Candidatelist=[]  
    # unique_list = []
    Candidate_Votes = {}
    #Winning_Candidate and Winning Count Tracker 
    Winner = ""
    Winning_count = 0 
     
    for row in csvreader:
        print(",",end="")
        total_votes=total_votes + 1 
        candidate_name=row[2]

        if candidate_name not in Candidate_Options:
            Candidate_Options.append(candidate_name)
            Candidate_Votes[candidate_name]= 0 
        Candidate_Votes[candidate_name]=Candidate_Votes[candidate_name] +1

    with open(output_file,"w") as txt_file:
        election_results=(f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
        print(election_results, end="")
        txt_file.write(election_results)

        for candidate in Candidate_Votes:
            votes=Candidate_Votes.get(candidate)
            vote_percentage=float(votes)/float(total_votes)*100
            #determine the winning count vote and candidate 

            if(votes > Winning_count):
                Winning_count=votes
                winner=candidate           
            voter_output=f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
            print(voter_output, end="")
            txt_file.write(voter_output)

            summary_of_winning_candidates=(
            f"-------------------------\n"
            f"Winner: {winner}\n"
            f"-------------------------\n")
            # txt_file.write(summary_of_winning_candidates)

        print(summary_of_winning_candidates)
        txt_file.write(summary_of_winning_candidates)

# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette

