import matplotlib.pyplot as plt

columns = ('Alternative', 'Frequency', 'Frequency Distribution')
data_cell_text = [
    ['A', 60, 60 / 120],
    ['B', 24, 24 / 120],
    ['C', 36, 36 / 120]
]

the_table = plt.table(cellText=data_cell_text,
                      colLabels=columns, loc='center')
plt.axis('off')
plt.grid('off')

plt.show()
