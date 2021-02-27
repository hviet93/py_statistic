import matplotlib.pyplot as plt

columns = ('Alternative', 'Frequency')
cell_text = [
    ['A', 200 * 0.22],
    ['B', 200 * 0.18],
    ['C', 200 * 0.40],
    ['D', 200 * 0.2]
]

the_table = plt.table(cellText=cell_text, colLabels=columns, loc='center')
plt.axis('off')
plt.grid('off')

plt.show()
