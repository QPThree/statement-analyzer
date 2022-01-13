# Statement-Analyzer

## Version
* ### v1.0.0

## Authors

 * Quentin Young

## Motivation

To get a personalized visualization of monthly credit card spending and personal financing.

## Description

The Statement-Analyzer will look at a users credit card statement and give the user visuals of their spending for the month. Version 1.0.0 gives the user a categorical pie chart of their spending.

## Tech

* Python3
* Pandas
* matplotlib
* git

## How-To
1. Save credit card .xlsx files in the statements folder of the statement analyzer directory 
2. To run : Navigate to statement analyzer directory and in cli run "python3 analyzer.py < Month >" 
3. Terminal will give proof of completion and save. Visuals can be found in the "output" folder within the statement analyzer directory

NOTE: Statements must be saved in "statement-analyzer/statements" folder

NOTE: Current naming convention for statements is "MonthStatement.xlsx" (e.g. JuneStatement.xlsx)

### Example command line entry

> \>python3 analyzer.py january

#### help 

> \>python3 analayzer.py -h