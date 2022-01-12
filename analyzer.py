#!/usr/bin/python3
"""Docs comment here"""

from HighestChargesFactory import HighestChargesFactory  # Pie chart from matplotlib docs
from PieChartFactory import PieChartFactory
import sys #for cli

def main():

    selected_month = get_month_from_args() #Now comes from command line
    excel_file = get_excel_file(selected_month) #Access to relevant data

    # Calls to data vis file creations
    HighestChargesFactory(excel_file, selected_month)
    PieChartFactory(excel_file, selected_month)

def get_month_from_args():
     #TODO: Add checks here. Maybe make into selectabel list?
    selected_month = str(sys.argv[1])
    return selected_month

def get_excel_file(selected_month):
    return f'statements/{selected_month}Statement.xlsx'

if __name__ == "__main__":
    main()
