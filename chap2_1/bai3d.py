import matplotlib.pyplot as plt

plt.style.use('ggplot')

x = ['Yes', 'No', 'No Opinion']
data = [58, 42, 20]

x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, data, color='green')
plt.xlabel('Answers')
plt.ylabel('Quantities')

plt.xticks(x_pos, x)

plt.show()
