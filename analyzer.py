#!/usr/bin/python3
"""Analyzer.py executed at runtime"""
import argparse
from HighestChargesFactory import HighestChargesFactory
from PieChartFactory import PieChartFactory

def main():
    parser = argparse.ArgumentParser(description='Enter month of statement to analyze')
    parser.add_argument('selected_month',  help='e.g. December')
    args = parser.parse_args()
    excel_file = get_excel_file(args.selected_month) #Access to relevant data

    # Calls to data vis file creations
    HighestChargesFactory(excel_file, args.selected_month)
    PieChartFactory(excel_file, args.selected_month)

def get_excel_file(selected_month):
    return f'statements/{selected_month}Statement.xlsx'

if __name__ == "__main__":
    main()
