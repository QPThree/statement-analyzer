import pandas as pd
import matplotlib.pyplot as plt
import os

from FileSaver import FileSaver


class HighestChargesFactory(FileSaver):

    def __init__(self, file, month):
        self.purchases = []
        self.data = []
        self.month = month
        self.config_data_table(file)

    def config_data_table(self, excel_file):
        statement_data = pd.read_excel(excel_file, sheet_name=0, index_col=0).sort_values('amount', ascending=False).head(5)
        for index, row in statement_data.head(5).iterrows():
            self.purchases.append(row['purchase'])
            self.data.append([row['purchase'],row['amount'], row['category']])
        fig, ax = plt.subplots()
        rank = self.fill_rank()
        ax.set_axis_off()
        table = ax.table(
            colLabels = statement_data.columns.tolist(),
            rowLabels = rank,
            cellText = self.data)
        self.save_figure(self.month,plt, "Top5")

    def fill_rank(self):
        rankarr = []
        i = 1
        for x in self.data:
            rankarr.append(i)
            i += 1
        return rankarr