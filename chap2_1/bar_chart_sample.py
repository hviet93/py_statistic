import matplotlib.pyplot as plt

# %matplotlib inline
plt.style.use('ggplot')

x = ['Nuclear', 'Hydro', 'Gas', 'Oil', 'Coal', 'Biofuel']
energy = [5, 6, 15, 22, 24, 8]

x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, energy, color='green')
plt.xlabel("Energy Source")
plt.ylabel("Energy Output (GJ)")
plt.title("Energy output from various fuel sources")

plt.xticks(x_pos, x)

plt.show()

# (B) Business, (CSE) Computer Sciences and Engineering, (E) Education,
# (H) Humanities, (NSM) Naturel Sciences and Mathematics,
# (SBS) Social and Behavioral Sciences, (O) Other
