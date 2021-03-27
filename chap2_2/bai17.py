import matplotlib.pyplot as plt

# 0 1 2 3 4
# 5 6 7 8 9
# 10 11 12 13 14
# 15 16 17 18 19
# 20 21 22 23 24

data = [
    2, 5, 10, 12, 4, 4, 5, 17, 11, 8, 9, 8,
    12, 21, 6, 8, 7, 13, 18, 3
]
data_class = {
    '0_4': {
        'label': '0 - 4',
        'freq': 0,
        'per_freq': 0.0
    },
    '5_9': {
        'label': '5 - 9',
        'freq': 0,
        'per_freq': 0.0
    },
    '10_14': {
        'label': '10 - 14',
        'freq': 0,
        'per_freq': 0.0
    },
    '15_19': {
        'label': '15 - 19',
        'freq': 0,
        'per_freq': 0.0
    },
    '20_24': {
        'label': '20 - 24',
        'freq': 0,
        'per_freq': 0.0
    }
}
plt.figure(dpi=1200)
fig, ax = plt.subplots(1, 1)
ax.axis('tight')
ax.axis('off')


def calc_data():
    for key in data_class:
        min_val = int(key.split("_")[0])
        max_val = int(key.split("_")[1])

        for val in data:
            if min_val <= val <= max_val:
                data_class[key]['freq'] += 1

        data_class[key]['per_freq'] = data_class[key]['freq'] / 20


def show_table_data():
    column_labels = ["Waiting Time", "Frequency Distribution", "Relative Frequency Distribution"]
    table_data = []

    for key in data_class:
        sub_data = [
            data_class[key]['label'], data_class[key]['freq'],
            data_class[key]['per_freq']
        ]
        table_data.append(sub_data)

    table_data.append(['Total', 20, 1.0])
    ax.table(cellText=table_data, colLabels=column_labels, loc="center")

    plt.show()


def show_cumulative_table_data():
    column_labels = ["Waiting Time", "Cumulative Frequency Distribution", "Relative Cumulative Frequency Distribution"]
    table_data = []
    total = 0

    for key in data_class:
        total += data_class[key]['freq']
        sub_data = [
            data_class[key]['label'], total, total / 20
        ]
        table_data.append(sub_data)

    ax.table(cellText=table_data, colLabels=column_labels, loc="center")

    plt.show()


def main():
    calc_data()
    # show_table_data()
    show_cumulative_table_data()


main()
