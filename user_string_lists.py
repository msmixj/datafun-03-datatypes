"""
Susie Smith
February 2, 2023 
Examples of using string lists that pertain to my domain: Basketball

Task 4. String Lists

"""
print('=========================================')
print('Task 4. String Lists')
print('----------------------')
print()

#imports first
import random

#Generate 5 lists:
#Player names
#types of defense
#offensive plays
#practice drills

players = ["Cora", "Elle", "Sydney", "Paisley", "Kaylynn", "Jordyn", "Kinley"]

defense = ["2-3 zone", "man-to-man", "1-2-2 zone", "box-and-one"]

offensive_plays = ["Iowa", "4-out", "hot fudge", "Bulldog-1", "Bulldog-5"]

practice_drills = ["defensive shuffle", "3-on-2", "shell drill", "Mikan drill"]

fouls = ["charge", "block", "illegal screen", "technical", "intentional", "flagrant"]

#String Lists 1. Using Python Built-In Functions
print("String Lists 1. Using Python Built-In Functions")
print(' 1.Use the built-in functions: len(), set(), and zip() to combine 2 or more lists into tuples.')
print(f'    len(): Our basketball team has {len(players)} players.')
print(f'    set(): We will focus on these drills at practice: {set(practice_drills)}')
print('    zip():')
for defense, offensive_plays in zip(defense, offensive_plays):
    print(f'        When the other team plays {defense} defense, we will run {offensive_plays}')
print()
print('------------------')
print('String Lists 2. Random Choice')

#Random choice to pick a random value from one of my lists
print(f'    1.Use random.choice to pick a random player: {random.choice(players)}')

#Random sentence generator:
#Name the player to start the game as point guard. The first play of the game will be the offensive play.
#We will make sure that we play well and keep our types of fouls to a minimum.
print(f'    2.Customize the sentence generator to create random sentences about your domain:')
sentence1 = (
    f"{random.choice(players)} will start the game as point guard."
)
sentence2 = (
    f"We will start the game in a {random.choice(defense)} defense and {random.choice(offensive_plays)} offense."
)
sentence3 = (
    f"We will make sure that we play well and keep our {random.choice(fouls)} fouls to a minimum."
)

print()
print(sentence1)
print(sentence2)
print(sentence3)
print()

print('----------------------')
print("String Lists 3. Get Unique Words")
print('  1.Choose one of the text data files in the repo: text_names_in.txt')
print('  2.See code for using open(), read(), split(), and set() to read a text file')
#2.Use open(), read(), split(), and set() to read a text file and get a unique list of words.
with open("text_names_in.txt", "r") as file:
    text = file.read()
    list_words = text.split()
    unique_words = set(list_words)

print(f'  3.Sort the list: {sorted(unique_words)}')
print(f'  4.The number of unique words in the Names text file is {len(unique_words)}.')
print('   5. The list is very busy!')
print()



# call functions and execute code
# use if __name__ == "__main__":
