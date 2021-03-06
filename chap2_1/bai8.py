import matplotlib.pyplot as plt
from chap2_1.bai5 import ExportData

# (P) Pitcher, (H) Catcher, (1) 1st base, (2) 2nd base, (3) 3rd base, (S) Shortstop,
# (L) Left field, (C) Center Field, (R) Right Field

export_data = ExportData('baseballhall.xlsx')
export_data.row_idx = 1
data_input = {
    'p': {
        'freq': 0,
        'per_freq': 0
    },
    'h': {
        'freq': 0,
        'per_freq': 0
    },
    '1': {
        'freq': 0,
        'per_freq': 0
    },
    '2': {
        'freq': 0,
        'per_freq': 0
    },
    '3': {
        'freq': 0,
        'per_freq': 0
    },
    's': {
        'freq': 0,
        'per_freq': 0
    },
    'l': {
        'freq': 0,
        'per_freq': 0
    },
    'c': {
        'freq': 0,
        'per_freq': 0
    },
    'r': {
        'freq': 0,
        'per_freq': 0
    }
}
export_data.change_data_input(data_input)

def show_table_freq():
    fig, ax = plt.subplots(1, 1)
    column_labels = ["Position", "Relative Frequency", "Percent Frequency"]
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
