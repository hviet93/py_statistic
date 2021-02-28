import matplotlib.pyplot as plt
from chap2_1.bai5 import ExportData

# ABC, CBS, FOX, NBC
export_data = ExportData('2012networks.xlsx')
data_input = {
    'abc': {
        'freq': 0,
        'per_freq': 0
    },
    'cbs': {
        'freq': 0,
        'per_freq': 0
    },
    'fox': {
        'freq': 0,
        'per_freq': 0
    },
    'nbc': {
        'freq': 0,
        'per_freq': 0
    }
}
export_data.change_data_input(data_input)


def show_table_freq():
    fig, ax = plt.subplots(1, 1)
    column_labels = ["Shows", "Relative Frequency", "Percent Frequency"]
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


def show_bar_chart():
    data = export_data.data_input
    plt.style.use('ggplot')
    show_name = []
    show_data = []

    for key in data:
        show_name.append(str(key).upper())
        show_data.append(data[key]['freq'])

    x_pos = [i for i, _ in enumerate(show_name)]
    plt.bar(x_pos, show_data, color='green')
    plt.xlabel('Show Name')
    plt.ylabel('Frequency')

    plt.xticks(x_pos, show_name)
    plt.show()


show_table_freq()
# show_bar_chart()
