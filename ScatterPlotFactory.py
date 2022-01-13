import pandas as pd
import matplotlib.pyplot as plt
import os

from FileSaver import FileSaver


class ScatterPlotFactory(FileSaver):

    def __init__(self, file, month):
        self.data ={"date":[], "amount":[]}
        self.month = month
        self.config_scatter_plot(file)
    
    def config_scatter_plot(self, file):
        statement_data = pd.read_excel(file, sheet_name=0, index_col=False)
        for index, row in statement_data.iterrows():
            self.data["date"].append(row['date'])
            self.data["amount"].append(row['amount'])
        
        df = pd.DataFrame(data = self.data)
        df.plot.scatter(x = 'date', y='amount', s = 'amount', c = 'green')
        self.save_figure(self.month, plt, "ScatterPlot")