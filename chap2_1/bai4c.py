import matplotlib.pyplot as plt
from chap2_1.bai4b import ExportData

export_data = ExportData()
show_name = export_data.get_data_label()

# Pie chart
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('equal')
ax.pie(export_data.freq_data, labels=show_name, autopct='%1.2f%%')

# Bar chart
# plt.style.use('ggplot')
# x_pos = [i for i, _ in enumerate(show_name)]
#
# plt.bar(x_pos, export_data.freq_data, color='green')
# plt.xlabel('Show Name')
# plt.ylabel('Frequency')
# plt.xticks(x_pos, show_name)

plt.show()
