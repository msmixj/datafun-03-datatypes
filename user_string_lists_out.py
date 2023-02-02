"""
Microsoft Windows [Version 10.0.22621.1105]
(c) Microsoft Corporation. All rights reserved.

C:\Users\15152\Documents\datafun-03-datatypes>C:/Users/15152/miniconda3/Scripts/activate

(base) C:\Users\15152\Documents\datafun-03-datatypes>conda activate base

(base) C:\Users\15152\Documents\datafun-03-datatypes>C:/Users/15152/miniconda3/python.exe c:/Users/15152/Documents/datafun-03-datatypes/user_strin
g_lists.py
=========================================
Task 4. String Lists
----------------------

String Lists 1. Using Python Built-In Functions
 1.Use the built-in functions: len(), set(), and zip() to combine 2 or more lists into tuples.
    len(): Our basketball team has 7 players.
    set(): We will focus on these drills at practice: {'3-on-2', 'shell drill', 'defensive shuffle', 'Mikan drill'}
    zip():
        When the other team plays 2-3 zone defense, we will run Iowa
        When the other team plays man-to-man defense, we will run 4-out
        When the other team plays 1-2-2 zone defense, we will run hot fudge
        When the other team plays box-and-one defense, we will run Bulldog-1

------------------
String Lists 2. Random Choice
    1.Use random.choice to pick a random player: Paisley
    2.Customize the sentence generator to create random sentences about your domain:

Kaylynn will start the game as point guard.
We will start the game in a x defense and g offense.
We will make sure that we play well and keep our block fouls to a minimum.

----------------------
String Lists 3. Get Unique Words
  1.Choose one of the text data files in the repo: text_names_in.txt
  2.See code for using open(), read(), split(), and set() to read a text file
  3.Sort the list: ['&', '(&', '10,000', '40', '42', 'A', 'A-Ha', 'ABC', 'AC/DC', 'Abdul', 'Accept', 'Adam', 'Adams', 'Aerosmith', 'Afrika', 'Air'
, 'Alan', 'Anita', 'Ant', 'Aretha', 'Asia', "B-52's", 'B.', 'Baker', 'Ballet', 'Bambaataa', 'Bananarama', 'Bangles', 'Beastie', 'Benatar', 'Berlin
', 'Billy', 'Black', 'Block', 'Blondie', 'Bob', 'Bobby', 'Bon', 'Bonnie', 'Boogie', 'Boston', 'Bowie', 'Boys', 'Branigan', 'Brown', 'Bruce', 'Brya
n', 'Burgh', 'Cannibals', 'Cara', 'Cars', 'Cats', 'Chain', 'Chapman', 'Chicago', 'Chili', 'Chris', 'Cinderella', 'Clapton', 'Clash', 'Club', 'Coll
ins', 'Cool', 'Corey', 'Costello', 'Crosby', 'Crue', 'Cult', 'Culture', 'Cure', 'Cyndi', "D'arby", 'DJ', 'Dark', 'David', 'De', 'Dead', 'Debbie',
'Dee', 'Def', 'Depeche', 'Dio', 'Dire', 'Dokken', 'Don', 'Double', 'Doug', 'Down', 'Duran', 'DÃ¼', 'E.', 'Earth', 'Easton', 'Eddie', 'Eddy', 'Edit
ion', 'Elton', 'Elvis', 'Enemy', 'Eric', 'Estefan', 'Europe', 'Eurythmics', 'Falco', 'Farnham', 'Fears', 'Femmes', 'Fine', 'Fire', 'Five', 'Fixx',
 'Flag', 'Flash', 'Fleetwood', 'Flock', 'Floyd', 'Foreigner', 'Frankie', 'Franklin', 'Fresh', 'Furious', 'Gabriel', 'Gang', 'Gaye', 'Genesis', 'Ge
orge', 'Gibson', 'Gloria', "Go-Go's", 'Goes', 'Grandmaster', 'Grant', 'Guns', 'Halen', 'Hall', 'Hart', 'Heads', 'Heart', 'Heartbreakers', 'Henley'
, 'Hollywood', 'Hornsby', 'Hot', 'Houston', 'Howard', 'Huey', 'Human', 'HÃ¼sker', 'INXS', 'Idol', 'Irene', 'Iron', 'J', 'Jackson', 'Jam', 'James',
 'Janet', 'Jazzy', 'Jeff', 'Jesus', 'Jett', 'Joan', 'Joel', 'John', 'Jones', 'Journey', 'Jovi', 'Judas', 'KISS', 'Kennedys', 'Kenny', 'Kids', 'Koo
l', 'L.L.', 'La', 'LaBelle', 'Lauper', 'Laura', 'League', 'Lee', 'Lennon', 'Leppard', 'Level', 'Lewis', 'Lionel', 'Loggins', 'Loverboy', 'Luther',
 'Mac', 'Machine', 'Madness', 'Madonna', 'Maiden', 'Maniacs', 'Manoeuvres', 'Marvin', 'Marx', 'Mary', 'McCartney', 'Mellencamp', 'Men', 'Metallica
', 'Miami', 'Michael', 'Michael/Wham', 'Mike', 'Milli', 'Minds', 'Mister', 'Mode', 'Moe', 'Money', 'Motley', 'Mr.', "N'", 'N.W.A', 'Nash', 'New',
'News', 'Nicks', 'Oates', 'Ocean', 'Oldfield', 'Orchestral', 'Order', 'Osbourne', 'Ozzy', 'Palmer', 'Parsons', 'Pat', 'Patti', 'Paul', 'Paula', 'P
eppers', 'Pet', 'Pete', 'Peter', 'Petty', 'Phil', 'Pink', 'Pixies', 'Pointer', 'Poison', 'Police', 'Pretenders', 'Priest', 'Prince', 'Productions'
, 'Project', 'Public', 'Queen', 'Quiet', 'R.E.M.', 'RATT', 'REO', 'Raitt', 'Rakim', 'Range', 'Ray', 'Red', 'Replacements', 'Richard', 'Richie', 'R
ick', 'Riot', 'Robert', 'Rod', 'Rolling', 'Roses', 'Roth', 'Row', 'Run-D.M.C.', 'Rush', 'Sabbath', 'Sade', 'Salt-N-Pepa', 'Scorpions', 'Seagulls',
 'Seger', 'Sheena', 'Shop', 'Simon', 'Simple', 'Simply', 'Sister', 'Sisters', 'Skid', 'Slayer', 'Smiths', 'Sonic', 'Soul', 'Sound', 'Spandau', 'Sp
eedwagon', 'Springfield', 'Springsteen', 'Squeeze', 'Squier', 'Starship', 'Steve', 'Stevie', 'Stewart', 'Stills', 'Sting', 'Stone', 'Stones', 'Str
aits', 'Stray', 'Styx', 'Supply', 'Talking', 'Tears', 'Terence', 'The', 'Thompson', 'Thorogood', 'Tiffany', 'Tina', 'Tom', 'Tone-Loc', 'Top', 'Tot
o', 'Townshend', 'Tracy', 'Trent', 'Trouble', 'Turner', 'Twins', 'Twisted', 'U2', 'UB', 'Van', 'Vandross', 'Vanilli', 'Vaughan', 'Violent', 'Waits
', 'Whitesnake', 'Whitney', 'Wind', 'Winwood', 'Wonder', 'Work', 'Yes', 'Young', 'Young)', 'Youth', 'ZZ', 'and', 'at', 'for', 'in', 'of', 'on', 't
he', 'to']
  4.The number of unique words in the Names text file is 356.
   5. The list is very busy!
"""