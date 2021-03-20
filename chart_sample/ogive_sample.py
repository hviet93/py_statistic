# importing modules 
import numpy as np
import matplotlib.pyplot as plt

# creating dataset 
data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27]

# creating class interval 
classInterval = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# calculating frequency and class interval 
values, base = np.histogram(data, bins=classInterval)

# calculating cumulative sum 
cumsum = np.cumsum(values)

# plotting  the ogive graph 
plt.plot(base[1:], cumsum, color='red', marker='o', linestyle='-')

# formatting 
plt.title('Ogive Graph')
plt.xlabel('Marks in End-Term')
plt.ylabel('Cumulative Frequency')

plt.show()

# https://www.statology.org/ogive-python/
# def show_ogive(self):
#     values, base = np.histogram(self.data, bins=5)
#     plt.plot(base[:-1], self.cumulative_data, 'ro-')
#     plt.show()
