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
print('========================================================')
print('Task 3: Numeric Lists')
print()
"""
Create list of players' jersey numbers (list1)
Create list of 10 integers using range (listx)
Create list of total accumulated team points (listy)
"""

#List1 of players' jersey numbers
print("List 1 = Player Roster (Jersey Numbers):")

list1_roster = [0, 1, 2, 3, 4, 7, 8, 9, 10, 12, 16, 
              18, 19, 21, 22, 25, 29, 30, 32, 36, 48, 54]
print("List 1 is the roster of the basketball players' numbers.")
print(list1_roster)
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
print('-------------------------------------------')
print()

#Lists 1 Statistic functions
print("Lists 1: Statistics:")
print("  1.Calculate the mean, median, and mode")

#Function and print results of mean, median and mode
print(f'     Mean for List 1 = {round(stats.mean(list1_roster))},\
 Mean for List x = {round(stats.mean(listx))}, Mean for List y = {round(stats.mean(listy))}')
print(f'     Median for List 1 = {round(stats.median(list1_roster))},\
 Median for List x = {round(stats.median(listx))}, Median for List y = {round(stats.median(listy))}')
print(f'     Mode for List 1 = {stats.mode(list1_roster)},\
 Mode for List x = {stats.mode(listx)}, Mode for List y = {stats.mode(listy)}')
print()


#Function and print results of standard deviation and variance
print("  2.Calculate the standard deviation and variance")
print(f"""    Standard deviation for List 1 = {round(stats.stdev(list1_roster))}
    Standard deviation for List x = {round(stats.stdev(listx))}
    Standard deviation for List y = {round(stats.stdev(listy))}""")
print(f"""    Variance for List 1 = {round(stats.variance(list1_roster))}
    Variance for List x = {round(stats.variance(listx))}
    Variance for List y = {round(stats.variance(listy))}""")
print()
print('----------------------------')
print()

#Lists 2 Lists - Correlation and Prediction
print("Lists 2. Lists - Correlation and Prediction")

#Correlation and prediction
print("  1.Calculate the correlation between List x and List y")

#Return results here
print(f'    Correlation between List x and List y = {stats.correlation(listx, listy):.2f}')
print()

#Slope and intercept of best fit line
print("  2.Calculate the slope and intercept of the best fit line.")
slope, intercept = (stats.linear_regression(listx, listy))

#Return results here
print(f'    Slope and intercept of the best fit line is {round(slope)} and {round(intercept)}, respectively.')
slope, intercept = (stats.linear_regression(listx, listy))
print()

#Set a future time = 15
print("  3.Set a future time = 15")
x_future = 15
print()

#Predict y value at future time 
print("  4.Predict the y value at the future time y=mx+b where m is the slope and b is the y intercept")
y_future = ((slope * x_future) + intercept)
print(f'    The predicted y value at the future time (x = 15) is {round(y_future)}.')
print()
print('--------------------------')
print()
#Lists 3. Lists - Using Python Built-In Functions
"""Using information from List 1, I will calculate
built-in functions min, max, len, sum, avg, set, sort and sort using reverse order
"""
print("Lists 3. Lists - Using Python Built-In Functions")


list1_min = min(list1_roster)
list1_max = max(list1_roster)
list1_length = len(list1_roster)
list1_sum = sum(list1_roster)
list1_avg = list1_sum / list1_length
list1_set = set(list1_roster)
list1_sort = sorted(list1_roster)
list1_sort_rev = sorted(list1_roster, reverse=True)

print(f'  1.Minimum jersey number: {list1_min}')
print(f'  2.Maximum jersey number: {list1_max}')
print(f'  3.Player/Jersey count: {list1_length}')
print(f'  4.Sum of jersey numbers: {list1_sum}')
print(f'  5.Average of jersey numbers: {round(list1_avg)}')
print(f'  6.Jersey set {list1_set}')
print(f'  7.Jersey numbers sorted (Ascending): {list1_sort}')
print(f'  8.Jersey numbers sorted (Descending): {list1_sort_rev}')
print()

print('-----------------------------')
#Lists 4. List Methods
"""In this section I will make a new short list and explore list methods."""
print()

print("Lists 4. List Methods")
lst = [522, 516, 93, 1030, 729]
print(f'Lst: {lst}') 

#appending a list
lst.append(620) #created appended list
print(f'    1.append() a single value to the list:  {lst}')

#extending the list
lst.extend([112,33])
print(f'    2.extend() the list with a new list you pass in:  {lst}')


#insert at an index, insert a value
lst.insert(3, 5)
print(f'    3.insert() at an index, insert a value:  {lst}')


#remove(5), remove the number 5 from my list; first add number 5
lst.remove(5)
print(f'    4.remove(5), remove the number 5 from the list: {lst}')

#count(2), count how many times 2 appears in your list (if it doesn't change 2 to a value in your list)
lst.insert(4,2)
print('    5.count(2) count how many times 2 appears in your list')
lst.insert(5,2)
print(f'        Lst: {lst}')




      





# For example, if your domain:
# Is sports, create functions to provide a list of teams.
# Is pets, create functions to calculate adoption prices.
# Is music, create functions to return a list of your favorite artists.


# When you write reusable functions for your domain, you can
# import the module with your utility functions into other modules
# and use them there.  This is a very common practice.
# Anything you write can be imported into later projects.

