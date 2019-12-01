
#set up the master index that will be used to loop through each local election
master_index = 0
#set up all the ridings and order them properly in the list of all the regions, which will be used to       
toronto = {"M5T", "M5S", "M5L", "M5K"} 
vancouver = {"R5K", "R4W", "R1M", "R0T"}
brampton = {"L4T", 'L4H', 'L0P', 'L4M'}
montreal = {'H1A', 'H3A', 'H1B', 'H4X'}
calgary = {'T1X', 'T1Y', 'T2A', 'T2N'}
winnipeg = {'R0G', 'R2C', 'R2M', 'R3P'}
oshawa = {'L1B', 'L1E', 'L1G', 'L1H'}
victoria = {'V8P', 'V8N', 'V8R', 'V8T'}
yellowknife = {'P0B', 'P5K', 'P3I', 'P8M'}
master_region_list = [toronto, vancouver, brampton]
master_region_list_strings = ("Toronto", "Vancouver", "Brampton", "Montreal", "Calgary", "Winnipeg", "Oshawa", "Victoria", "Yellowknife")
#write out the seat count list which would change after each local election is finished, as well as the party_codes
#list which corresponds to each value in the seat count lsit (item 1 in the seat count list corresponds to conservatives)
seat_count_list = [0, 0, 0, 0]
party_codes = ["Conservatives", "Liberals", "NDP", "Green Party"]
print("Welcome to the federal election of 2023! This software will allow the votes to be tallied in the 9 ridings of Canada, and then calculate who wins the general election. Let's get started!")
#Set up a loop that does not finish until every local election has been completed
while not master_index == (len(master_region_list)) :
    #set up another loop that would determine the end of a local election
    if not master_index == 0:
        print("We'll now move on to the next riding, the city of " + master_region_list_strings[master_index])
        print()
    local_election_over = "false"
    while not local_election_over == "true":
        #set up another loop that would finish at the end of the voting process for the local election
        local_vote_over_pin = 0
        local_vote_count = [0, 0, 0, 0]
        while not local_vote_over_pin == '3311':
            #Begin the election by welcoming the voters, and validate age and postal code (according to current region)
            print("Welcome to the " + master_region_list_strings[master_index] + " federal riding!")
            voter_age = int(input("What is your age? "))
            if voter_age >= 18:
                print("Great, you are old enough to vote!")
                fsa_code = input("What are the first three characters of your postal code? ")
                if fsa_code in master_region_list[master_index]:
                    print("Great, you live in this riding!")
                    #Ask for the person's vote and then adjust the local vote count by their vote
                    current_vote_index = int(input("What party would you like to vote for? Type 0 for Conservatives, type 1 for Liberals, type 2 for NDP and type 3 for Green Party "))
                    if not current_vote_index in [0, 1, 2, 3]:
                        print("Invalid vote, you lost your shot!")
                    else: 
                        local_vote_count[current_vote_index] = local_vote_count[current_vote_index] + 1
                        print("Thanks for voting!")
                        #Ask if the current voter is actually an administrator to end the local election (all voters having voted)
                        administrator_access = input("Are you an administrator who would like to end this election? Type Y if so. ")
                        if administrator_access == "Y":
                            local_vote_over_pin = input("What is the pin to finish the vote? ")
                            if not local_vote_over_pin == '3311':
                                print("That's not the right pin number, we will continue the local election")
                else: 
                    print("You don't live in this city, therefore you are not eligible to vote here!")
            else: print("You are not old enough to vote, try again when you're older!")       
        #Compare values in the local votes list to see which items had the greatest number of votes, add the indexes of those items
        #to a list        
        local_vote_winner = 0
        for party_vote_count in local_vote_count:
            if party_vote_count >= local_vote_winner:                
                local_vote_winner = party_vote_count
        winning_indexes = []        
        winning_indexes = [i for i in range(len(local_vote_count)) if local_vote_count[i] == local_vote_winner]             
        #Pronounce the winner of the local election by evaluating the list of winning indexes
        # If there's no tie, set the parameters that move onto the next local vote (or finish the local voting process)
        if len(winning_indexes) == 1:
            print("We have a winner! The party that won the " + master_region_list_strings[master_index] + " riding is...")
            print("the " + party_codes[winning_indexes[0]] +"!")
            seat_count_list[winning_indexes[0]] = seat_count_list[winning_indexes[0]] + 1
            master_index = master_index + 1
            local_election_over = "true"
        #In the case where two or more parties have a winning number, this is pronounced and the local election restarts    
        else:
            tie_index = 1
            print("There's no clear winner of the " + master_region_list_strings[master_index] + " riding!")
            if len(winning_indexes) == 2:
                print("The " + party_codes[winning_indexes[0]] + " and the " +  party_codes[winning_indexes[1]] + " tied for the most votes, at " + str(local_vote_count[winning_indexes[0]])  + " each.")
            if len(winning_indexes) == 3:
                print("The " + party_codes[winning_indexes[0]] + "and the " +  party_codes[winning_indexes[1]] + "and the " + party_codes[winning_indexes[2]] + "tied for the most votes, at " + str(local_vote_count[winning_indexes[0]]) + " each.")
            if len(winning_indexes) == 4:
                print("All four parties had the same number of votes, at " + str(local_vote_count[winning_indexes[0]]) + " each.")
            print("We'll have to go back to the polls!")
            local_vote_over_pin = '0'
print()
print("That's all the ridings! Now let's see who gained the most seats in Parliament and will form a government")
max_value = 0
for party_vote_count in seat_count_list:
    if party_vote_count >= max_value:                
        max_value = party_vote_count
winning_indexes = []        
winning_indexes = [x for x in range(len(seat_count_list)) if seat_count_list[x] == max_value]
if len(winning_indexes) == 1:
    winning_percentage = round((seat_count_list[winning_indexes[0]]/len(master_region_list)) * 100)
    print("The " + party_codes[winning_indexes[0]] + " won the election with " + str(winning_percentage) + "% of the seats")
    if winning_percentage >= 50:
        print("Because they have more than half of the seats, they will form a majority government")
    else:
        print("Because they have less than half of the seats, they will form a minority government")
    print("Happy federal election everyone! See you again soon (but hopefully not too soon)!")
else:
    print("No one party has the most number of seats, therefore a government cannot be formed!")
    if len(winning_indexes) == 2:
        print("The " + party_codes[winning_indexes[0]] +  " and the " + party_codes[winning_indexes[1]] + " tied with the most seats, at " + str(seat_count_list[winning_indexes[0]]) + " each.")
    if len(winning_indexes) == 3:
        print("The " + party_codes[winning_indexes[0]] +  " and the " + party_codes[winning_indexes[1]] + " and the " + party_codes[winning_indexes[2]] +  " tied with the most seats, at " + str(seat_count_list[winning_indexes[0]]) + " each" )
    print("We'll have to organize another election, and hang in governmental purgatory until that day. See you next time!")
            
       
        
        
        
       
        