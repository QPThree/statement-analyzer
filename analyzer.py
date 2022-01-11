
#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Exploring using pandas to create dataframes, and output graphs"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from HighestCharges import HighestCharges  # Pie chart from matplotlib docs
matplotlib.use('Agg')

import sys

def main():
    #Prompts user for month entry
    selected_month = get_month_from_args() #Now comes from command line


    excel_file = f'statements/{selected_month}Statement.xlsx'
    HighestCharges(excel_file, selected_month)
    config_matplot_figure(excel_file) #configure our figure
    save_figure(selected_month)

    
# TODO Change name of this as it comes from command line
def get_month_from_args():
     #TODO: Add checks here. Maybe make into selectabel list?
    selected_month = str(sys.argv[1])
    print(selected_month)
    return selected_month

def config_matplot_figure(excel_file):
    statement_data = pd.read_excel(excel_file, sheet_name=0, index_col=0)
    # this is a unique set of categories
    categories = set(statement_data['category'].values)
    labels = list(categories)
      # DONE. Aggregate totals for each category
    values = {}
    for index, row in statement_data.iterrows():
        if row['category'] in values:
            values[row['category']] += row['amount']
        else:
            values[row['category']] = row['amount']
    sizes = list(values.values())
    fig1, axs = plt.subplots()

    # followign from matplotlib docs
    axs.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    axs.axis('equal')

def save_figure(selected_month):
    plt.savefig(f"output/{selected_month}", bbox_inches='tight')
    print("Your file has been saved!")

if __name__ == "__main__":
    main()
