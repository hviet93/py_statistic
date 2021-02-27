import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
recipe = ['Yes', 'No', 'No Opinion']
data = [58, 42, 20]
ax.pie(data, labels=recipe, autopct='%1.2f%%')
plt.show()
