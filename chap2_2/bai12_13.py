import numpy as np
import matplotlib.pyplot as plt


class CumulativeDataExport:
    def __init__(self):
        self.table_data = []
        self.data_input = {
            '10_19': {
                'label': 'Less or equal to 19',
                'freq': 10
            },
            '20_29': {
                'label': 'Less or equal to 29',
                'freq': 14
            },
            '30_39': {
                'label': 'Less or equal to 39',
                'freq': 17
            },
            '40_49': {
                'label': 'Less or equal to 49',
                'freq': 7
            },
            '50_59': {
                'label': 'Less or equal to 59',
                'freq': 2
            }
        }
        self.labels = []
        self.data = []
        self.cumulative_data = []

    def calc_data(self):
        total = 0

        for key in self.data_input:
            total += self.data_input[key]['freq']
            sub_data = [
                self.data_input[key]['label'],
                total, total / 50
            ]
            self.table_data.append(sub_data)
            self.cumulative_data.append(total)

        for key in self.data_input:
            self.labels.append(str(key).replace("_", " - "))
            self.data.append(self.data_input[key]['freq'])

    def show_table_data(self):
        fig, ax = plt.subplots(1, 1)
        column_labels = ["Group", "Cumulative Frequency", "Cumulative Relative Frequency"]
        ax.axis('tight')
        ax.axis('off')

        ax.table(cellText=self.table_data, colLabels=column_labels, loc="center")
        plt.show()

    def show_histogram(self):
        x_pos = [i for i, _ in enumerate(self.labels)]
        plt.bar(x_pos, self.data, color='green', width=1.0, edgecolor='black')
        plt.xticks(x_pos, self.labels)

        plt.show()

    def show_ogive(self):
        values, base = np.histogram(self.data, bins=5)
        plt.plot(base[:-1], self.cumulative_data, 'ro-')
        plt.show()


def main():
    export_data = CumulativeDataExport()
    export_data.calc_data()

    # export_data.show_table_data()
    # export_data.show_histogram()
    export_data.show_ogive()


main()
