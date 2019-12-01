# CSCA20---Sean-Wei-Jane---Federal-Election---Project
Here are some steps for you to know in how to operate the code:
1. The code is an election software that has two different types of people using the code: Voters and Administrators. The administrators only come in at one step of the code, which we will explain later. However, for the regular use of the code, imagine that each time the election cycles through a voter it is a NEW PERSON answering the questions (this means their age and possibly their FSA code are different).
2. Each city only has specific sets of FSA codes (the postal codes) associated with it. For the full length version of the code (more on that in the next number in the list) here are the cities and the FSA codes associated with them:
toronto = {"M5T", "M5S", "M5L", "M5K"} 
vancouver = {"R5K", "R4W", "R1M", "R0T"}
montreal = {'H1A', 'H3A', 'H1B', 'H4X'}
brampton = {"L4T", 'L4H', 'L0P', 'L4M'}
calgary = {'T1X', 'T1Y', 'T2A', 'T2N'}
winnipeg = {'R0G', 'R2C', 'R2M', 'R3P'}
oshawa = {'L1B', 'L1E', 'L1G', 'L1H'}
victoria = {'V8P', 'V8N', 'V8R', 'V8T'}
yellowknife = {'P0B', 'P5K', 'P3I', 'P8M'}
Therefore, if you are going through the Toronto election and the code asks "What are the first three letters of your postal code?" only M5T, M5S, M5L and M5K will allow you to move to the next step of the process.
3. If you would like to do a shortened version of the code, you can edit the master_region_list in line 14 and delete however many local elections you wish. The local election code lists through the sets in this list, therefore if you only leave three items (which are sets) in this list then it will only loop three three local elections. However, if you do this, then do not change the order of the sets, as this will mess up later parts of the code (so, for example, if you only want to have three local elections, delete from "brampton" onward without changing the order of toronto, vancouver, montreal). As well, the code functions best if you leave an odd number of local elections (as then the federal government can more easily be called a majority government or a minortiy government).
4. At the end of each voter casting their ballot it will ask if an administrator would like to finish the local election. You, as the operator of the code, can choose however many local ballots you wish to be cast before ending the election. When you do follow the prompt to end the local election, it will then ask for the pin. The pin for all the local elections is 3311: If you don't put in this pin when it asks you to end the code, it will go to the next voter for the same local election.
5. The only time the code should crash is if you enter non-integer inputs for the age of the voter and the code of the party they want to wish for. Therefore, enter integers for these questions.
6. In terms of references, lines 65 and 94 (which are essentially the same) in our code were patterned after a line of code one of us found by online. This is the website we found it from, and as you can tell, the structure of these two lines in our code is pretty much identical to the "Method #2" code on this website: https://www.geeksforgeeks.org/python-ways-to-find-indices-of-value-in-list/ 
7. Press the green arrow in Wing and have fun!
