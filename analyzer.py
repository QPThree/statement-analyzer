
#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Exploring using pandas to create dataframes, and output graphs"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt  # Pie chart from matplotlib docs
matplotlib.use('Agg')


def main():

    #Prompts user for month entry
    selected_month = get_month_from_user()

    excel_file = f'statements/{selected_month}Statement.xlsx'

    #statement_data = pd.read_excel(excel_file, sheet_name=0, index_col=0)
    config_matplot_figure(excel_file)
    save_figure(selected_month)

    

def get_month_from_user():
     #TODO: Add checks here. Maybe make into selectabel list?
    selected_month = input("Which month would you like to see data for?")
   
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
    # This now has totals
    print("VALUES:", values)
    print("LABELS:", labels)
    sizes = list(values.values())
    print("SIZES:", sizes)
    # 3. use matplotlib to display data

    fig1, ax1 = plt.subplots()

    # This from matplot lib docs
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.axis('equal')


    # print(statement_data.head())


def save_figure(selected_month):
    plt.savefig(f"saved/{selected_month}", bbox_inches='tight')

if __name__ == "__main__":
    main()
