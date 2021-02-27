import matplotlib.pyplot as plt
import datetime
import numpy as np
import pandas as pd

# a)
# gmData = [8.9, 9.0, 8.9, 8.8]
# fordData = [7.8, 7.7, 7.8, 7.9]
# chryslerData = [4.1, 4.2, 4.3, 4.6]
# toyotaData = [7.8, 8.3, 9.1, 9.6]
# yearData = ['2004', '2005', '2006', '2007']
# df = pd.DataFrame({
#     'x': yearData, 'gmData': gmData,
#     'fordData': fordData, 'chryslerData': chryslerData,
#     'toyotaData': toyotaData
# })
#
# plt.plot('x', 'gmData', data=df, label='General Motors')
# plt.plot('x', 'fordData', data=df, label='Ford')
# plt.plot('x', 'chryslerData', data=df, label='DaimlerChrysler')
# plt.plot('x', 'toyotaData', data=df, label='Toyota')
#
# plt.title('Car Quantity Of Each Car Manufacturer')
# plt.ylabel('Quantity (millions)')
# plt.xlabel('Year')
# plt.legend()
# plt.show()

# b)

carQuantityData = [8.8, 7.9, 4.6, 9.6]
carBrand = ['General Motors', 'Ford', 'DaimlerChrysler', 'Toyota']

plt.bar(carBrand, carQuantityData, color='green')
plt.ylabel('Car Quantity')
plt.xlabel('Car Brand Name')
plt.title('Car Quantity of each Brand in 2007')
plt.show()
