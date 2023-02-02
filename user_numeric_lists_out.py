"""
Microsoft Windows [Version 10.0.22621.1105]
(c) Microsoft Corporation. All rights reserved.

C:\Users\15152\Documents\datafun-03-datatypes>C:/Users/15152/miniconda3/Scripts/activate

(base) C:\Users\15152\Documents\datafun-03-datatypes>conda activate base

(base) C:\Users\15152\Documents\datafun-03-datatypes>C:/Users/15152/miniconda3/python.exe c:/Users/15152/Documents/datafun-03-datatypes/user_numer
ic_lists.py
========================================================
Task 3: Numeric Lists

List 1 = Player Roster (Jersey Numbers):
List 1 is the roster of the basketball players' numbers.
[0, 1, 2, 3, 4, 7, 8, 9, 10, 12, 16, 18, 19, 21, 22, 25, 29, 30, 32, 36, 48, 54]

List x = 10 Integer Times
List x is a list of 10 integer times
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

List y represents 10 values read at the times in List x.
List y represents 10 measurements of accumulated team points.
[0, 2, 5, 5, 8, 11, 15, 18, 22, 24]

-------------------------------------------
Lists 1: Statistics:
  1.Calculate the mean, median, and mode
     Mean for List 1 = 18, Mean for List x = 4, Mean for List y = 11
     Median for List 1 = 17, Median for List x = 4, Median for List y = 10
     Mode for List 1 = 0, Mode for List x = 0, Mode for List y = 5

  2.Calculate the standard deviation and variance
    Standard deviation for List 1 = 15
    Standard deviation for List x = 3
    Standard deviation for List y = 8
    Variance for List 1 = 226
    Variance for List x = 9
    Variance for List y = 71

----------------------------

Lists 2. Lists - Correlation and Prediction
  1.Calculate the correlation between List x and List y
    Correlation between List x and List y = 0.99

  2.Calculate the slope and intercept of the best fit line.
    Slope and intercept of the best fit line is 3 and -1, respectively.

  3.Set a future time = 15

  4.Predict the y value at the future time y=mx+b where m is the slope and b is the y intercept
    The predicted y value at the future time (x = 15) is 40.

--------------------------
Lists 3. Lists - Using Python Built-In Functions
  1.Minimum jersey number: 0
  2.Maximum jersey number: 54
  3.Player/Jersey count: 22
  4.Sum of jersey numbers: 406
  5.Average of jersey numbers: 18
  6.Jersey set {0, 1, 2, 3, 4, 7, 8, 9, 10, 12, 16, 18, 19, 21, 22, 25, 29, 30, 32, 36, 48, 54}
  7.Jersey numbers sorted (Ascending): [0, 1, 2, 3, 4, 7, 8, 9, 10, 12, 16, 18, 19, 21, 22, 25, 29, 30, 32, 36, 48, 54]
  8.Jersey numbers sorted (Descending): [54, 48, 36, 32, 30, 29, 25, 22, 21, 19, 18, 16, 12, 10, 9, 8, 7, 4, 3, 2, 1, 0]

-----------------------------
Lists 4. List Methods
Lst: [522, 516, 93, 1030, 729]
    1.append() a single value to the list:  [522, 516, 93, 1030, 729, 620]
    2.extend() the list with a new list you pass in:  [522, 516, 93, 1030, 729, 620, 112, 33]
    3.insert() at an index, insert a value:  [522, 516, 93, 5, 1030, 729, 620, 112, 33]
    4.remove(5), remove the number 5 from the list: [522, 516, 93, 1030, 729, 620, 112, 33]
    5.count(2) count how many times 2 appears in your list
        lst: [522, 516, 93, 1030, 2, 2, 729, 620, 112, 33]
        The value 2 appears in lst 2 times.
    6.sort() lst: [2, 2, 33, 93, 112, 516, 522, 620, 729, 1030]
    7.sort(), with reverse: [1030, 729, 620, 522, 516, 112, 93, 33, 2, 2]
    8.copy() lst: [1030, 729, 620, 522, 516, 112, 93, 33, 2, 2]
    9.pop() first item off the top of the list: [729, 620, 522, 516, 112, 93, 33, 2, 2]
    10.pop() last item off the bottom of the list: [729, 620, 522, 516, 112, 93, 33, 2]

---------------------------------
Lists 5. List Transformations - Using filter() and map()
    1.Use filter()function to keep x such that x is an even value: [0, 2, 4, 8, 10, 12, 16, 18, 22, 30, 32, 36, 48, 54]
    2.Use map function to map each x to cuberoot of x: [0, 1, 8, 27, 64, 343, 512, 729, 1000, 1728, 4096, 5832, 6859, 9261, 10648, 15625, 24389, 2
7000, 32768, 46656, 110592, 157464]
    3.Use map funciton for volume of cube with side equal to value in list: [0, 1, 8, 27, 64, 343, 512, 729, 1000, 1728, 4096, 5832, 6859, 9261, 1
0648, 15625, 24389, 27000, 32768, 46656, 110592, 157464]

-------------------------------
Lists 6. List Transformations - Using List Comprehension
    3.List comprehension filter for list1, to get x if x < 4: [0, 1, 2, 3]
    4.Triple each value in list1: [0, 3, 6, 9, 12, 21, 24, 27, 30, 36, 48, 54, 57, 63, 66, 75, 87, 90, 96, 108, 144, 162]
    5.Transform jersey numbers list to show what numbers are available for new players joining the team: [1, 2, 3, 4, 5, 8, 9, 10, 11, 13, 17, 19,
 20, 22, 23, 26, 30, 31, 33, 37, 49, 55]

(base) C:\Users\15152\Documents\datafun-03-datatypes>
"""