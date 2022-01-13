import pandas as pd
import matplotlib.pyplot as plt
import os


class ScatterPlotFactory:

    def __init__(self, file, month):
        self.data ={"date":[], "amount":[]}
        self.config_scatter_plot(file)
        self.save_figure(month)
    
    def config_scatter_plot(self, file):
        statement_data = pd.read_excel(file, sheet_name=0, index_col=False)
        for index, row in statement_data.iterrows():
            self.data["date"].append(row['date'])
            self.data["amount"].append(row['amount'])
        
        df = pd.DataFrame(data = self.data)
        df.plot.scatter(x = 'date', y='amount', s = 'amount', c = 'green')

    def save_figure(self, selected_month):
        DIR = (selected_month)
        CHECK_FOLDER = os.path.isdir(f"output/{DIR}")

        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(f"output/{DIR}")

        plt.savefig(f"output/{selected_month}/Scatter", bbox_inches='tight')
        print("Your Scatter Chart has been saved!")