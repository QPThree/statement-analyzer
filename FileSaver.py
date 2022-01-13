import os, matplotlib

class FileSaver:
    def save_figure(self, selected_month, plt, charttype):
        DIR = (selected_month)
        CHECK_FOLDER = os.path.isdir(f"output/{DIR}")

        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(f"output/{DIR}")

        plt.savefig(f"output/{selected_month}/{charttype}", bbox_inches='tight')
        print(f"Your {charttype} Chart has been saved!")