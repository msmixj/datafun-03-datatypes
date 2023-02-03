"""
Susie Smith
February 2, 2023
Using Tuples and More

"""

print('================================================')
print('Task 5. Tuples and More)')
print("Practicing with tuples")

#Create some tuples
Cora_pointspergame = (5, 10, 23, 12, 8, 17)
Elle_pointspergame = (12, 17, 5, 10, 8, 10)


# tuple concatenation
tupleCat = Cora_pointspergame + Elle_pointspergame

# tuple repetition
tupleAThrice = Cora_pointspergame * 3

# TODO: Start using this f-string "syntactic sugar" for quick ouptut
# just add space = space inside the curly braces
# it will print the name of the variable and the value
print(f"{Cora_pointspergame = }")
print(f"{Elle_pointspergame = }")
print(f"{tupleCat = }")
print(f"{tupleAThrice = }")

# tuple membership testing

Jordyn_pointspergame = (10, 5, 3, 16, 10, 8)
hasTen = 10 in Jordyn_pointspergame  # True
hasTwenty = 20 in Jordyn_pointspergame  # False


# tuple indexing (0 is first, -1 is last, or 1 less than the length)

team_tuple = (20, 30, 40, 35, 30, 27)
first = team_tuple[0]
second = team_tuple[1]
third = team_tuple[2]
last = team_tuple[-1]
print()
print(f'The total points scored in the first game was {first}')
print(f'The total points scored in the last game was {last}')
print()

# Use tuples to return multiple values from a function

def divide_and_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder


q, r = divide_and_remainder(10, 3)
print(f"Quotient: {q}, Remainder: {r}")

print('--------------------------------------')
"""
SETS .......................................................    

"""
print('Sets')

TeamA = {2, 4, 6, 8, 10}
TeamB = {1, 2, 3, 4, 5, 6}

# set union
TeamC = TeamA | TeamB
print(TeamC)

# set intersection
TeamD = TeamA & TeamB
print(TeamD)

# set difference
TeamE = TeamA - TeamB
print(TeamE)

# sets are often used to remove duplicates from a list
# after gettin the set, convert it back to a list with list() or []

listWords = ["basketball", "hoop", "defense", "offense", "free throw", "jump ball"]
setWords = set(listWords)
listWordsNoDuplicates = list(setWords)
listWordsNoDuplicates = [setWords]  # same as above


print('------------------------------------')
print('Dictionaries')

playerA_dict = {"name": "Cora", "number": 4, "ppg": 13}
playerB_dict = {"name": "Elle", "number": 23, "ppg": 15}

assessment_dict = {"low": 0, "medium": 1, "high": 2}

data_dict = {
    "name": ["Cora", "Elle", "Jordyn", "Kinley"],
    "points": [10, 15, 13, 7],
    "rebounds": [4, 5, 2, 3],
}
print(data_dict)

with open("text_woodchuck.txt") as file_object:
    word_list = file_object.read().split()

word_counts_dict = {}
for word in word_list:
    if word in word_counts_dict:
        word_counts_dict[word] += 1
    else:
        word_counts_dict[word] = 1
print()

print(word_counts_dict)


# IMPORTANT: Dictionary comprehesions - the preferred approach

# Create a dictionary of word counts from a list of words
# A dictionary is alawys key:value pairs
# Say "I want word:count for each word in word_list"
# Remember to wrap the result in curly braces
word_counts_dict = {word: word_list.count(word) for word in word_list}

# Spend most of your practice on comprehensions - they are
# key to transforming data in Python.
