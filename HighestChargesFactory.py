import pandas as pd
import matplotlib.pyplot as plt


class HighestChargesFactory:

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
        self.save_figure(self.month)

    def fill_rank(self):
        rankarr = []
        i = 1
        for x in self.data:
            rankarr.append(i)
            i += 1
        return rankarr

    def save_figure(self, selected_month):
        plt.savefig(f"output/{selected_month}Top5", bbox_inches='tight')
        print("Top charges file has been saved!")