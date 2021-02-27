import matplotlib.pyplot as plt

columns = ('Alternative', 'Frequency', 'Percent Frequency Distribution (%)')
cell_text = [
    ['A', 200 * 0.22, 0.22 * 100],
    ['B', 200 * 0.18, 0.18 * 100],
    ['C', 200 * 0.40, 0.40 * 100],
    ['D', 200 * 0.2, 0.2 * 100]
]

the_table = plt.table(cellText=cell_text, colLabels=columns, loc='center')
plt.axis('off')
plt.grid('off')

plt.show()
