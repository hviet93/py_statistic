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

    def calc_data(self):
        total = 0

        for key in self.data_input:
            total += self.data_input[key]['freq']
            sub_data = [
                self.data_input[key]['label'],
                total, total / 50
            ]
            self.table_data.append(sub_data)

    def show_table_data(self):
        fig, ax = plt.subplots(1, 1)
        column_labels = ["Group", "Cumulative Frequency", "Cumulative Relative Frequency"]
        ax.axis('tight')
        ax.axis('off')

        ax.table(cellText=self.table_data, colLabels=column_labels, loc="center")
        plt.show()

    def show_histogram(self):
        labels = []
        data = []

        for key in self.data_input:
            labels.append(str(key).replace("_", " - "))
            data.append(self.data_input[key]['freq'])

        # x_pos = [i for i, _ in enumerate(labels)]
        fig, (ax1) = plt.subplots(nrows=1)
        ax1.hist(data, cumulative=True)

        plt.show()


def main():
    export_data = CumulativeDataExport()
    export_data.calc_data()

    # export_data.show_table_data()
    export_data.show_histogram()


main()
