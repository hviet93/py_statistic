import matplotlib.pyplot as plt
from chap2_1.bai5 import ExportData

# Excellent (E), Very Good (V), Good (G), Fair (F), Poor (P)
export_data = ExportData('airsurvey.xlsx')
data_input = {
    'e': {
        'freq': 0,
        'per_freq': 0
    },
    'v': {
        'freq': 0,
        'per_freq': 0
    },
    'g': {
        'freq': 0,
        'per_freq': 0
    },
    'f': {
        'freq': 0,
        'per_freq': 0
    },
    'p': {
        'freq': 0,
        'per_freq': 0
    }
}
export_data.change_data_input(data_input)


def show_table_freq():
    fig, ax = plt.subplots(1, 1)
    column_labels = ["Flight Rating", "Relative Frequency", "Percent Frequency"]
    ax.axis('tight')
    ax.axis('off')
    table_data = []
    total_freq = 0

    for key in export_data.data_input:
        sub_data = [str(key).upper(), export_data.data_input[key]['freq'], export_data.data_input[key]['per_freq']]
        total_freq += export_data.data_input[key]['freq']
        table_data.append(sub_data)

    table_data.append(['Total', total_freq, 100])
    ax.table(cellText=table_data, colLabels=column_labels, loc="center")
    plt.show()


show_table_freq()
