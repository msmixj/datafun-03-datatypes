"""
Susie Smith
January 31, 2023
Data Analytics Fundamentals Project 3
Domain: Basketball

The goal of this project is to make use of common data structures
and their usages.
In this project, I will be using lists, tuples, dictionaries, and sets.
I will also use Python built-in functions to filter items and map elements
to a new values.
"""

# import some modules first - how many can you make use of?

import math
import statistics as stats

"""Functions will be created for my domain of basketball."""
print('-----------------------------------------------')
print('Task 3: Numeric Lists')
print()
"""
Create list of players' jersey numbers (list1)
Create list of 10 integers using range (listx)
Create list of total accumulated team points (listy)
"""

#List1 of players' jersey numbers
print("List 1 = Player Roster (Jersey Numbers):")

list1_roster = [00, 1, 2, 3, 4, 7, 8, 9, 10, 12, 16, 
              18, 19, 21, 22, 25, 29, 30, 32, 36, 48, 54]
print("List 1 is the roster of the basketball players' numbers.")
print(list1_roster)
print()
print()

#Listx of 10 integer times (using range)
print("List x = 10 Integer Times")

listx = list(range(10))
print('List x is a list of 10 integer times')
print(listx)
print()

#List y representing 10 measurements of accumulated team points.
print("List y represents 10 values read at the times in List x.")
print("List y represents 10 measurements of accumulated team points.")

listy = [0,2,5,5,8,11,15,18,22,24,]
print(listy)
print()

#Lists 1 Statistic functions
print("Lists 1: Statistics:")
print("  1.Calculate the mean, median, and mode")

#Function and print results of mean, median and mode
print(f'     Mean for List 1 = {stats.mean(list1_roster)},\
 Mean for List x = {stats.mean(listx)}, Mean for List y = {stats.mean(listy)}')
print(f'     Median for List 1 = {stats.median(list1_roster)},\
 Median for List x = {stats.median(listx)}, Median for List y = {stats.median(listy)}')
print(f'     Mode for List 1 = {stats.mode(list1_roster)},\
 Mode for List x = {stats.mode(listx)}, Mode for List y = {stats.mode(listy)}')
print()

#Lists 2 standard deviation and variance
print("  2.Calculate the standard deviation and variance")


# For example, if your domain:
# Is sports, create functions to provide a list of teams.
# Is pets, create functions to calculate adoption prices.
# Is music, create functions to return a list of your favorite artists.


# When you write reusable functions for your domain, you can
# import the module with your utility functions into other modules
# and use them there.  This is a very common practice.
# Anything you write can be imported into later projects.

