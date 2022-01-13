import pandas as pd
import matplotlib.pyplot as plt
import os

from FileSaver import FileSaver

class PieChartFactory(FileSaver):

    def __init__(self, excel_file, selected_month):
        self.config_matplot_figure(excel_file, selected_month)
        #self.save_figure(selected_month)

    def config_matplot_figure(self, excel_file, selected_month):
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

        # following from matplotlib docs
        axs.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        axs.axis('equal')
        self.save_figure(selected_month,plt, "Pie")