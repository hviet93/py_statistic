import numpy

# 3
totalHotel = 9
rooms = [18, 166, 54, 47, 326, 45, 120, 10, 22]
commonRatedScore = [83.6, 86.3, 77.8, 76.8, 80.9, 73.7, 85.5, 76.9, 90.6]

# 3a Means value of room prices
meanRoom = numpy.mean(rooms)
print('Mean value of rooms')
print(meanRoom)  # 89.78
print('-----------------------------')

# 3b Mean value of Common rated score
meanTotalScore = numpy.mean(commonRatedScore)
print('Total score')
print(meanTotalScore)
print('-----------------------------')

# 3c Percentage of the hotel stay at England
englandHotel = 2
percentLocation = (englandHotel * 100) / 9
print('Percentage of the hotel stay at England')
print(percentLocation)
print('-----------------------------')

# 3d Percentage of the hotel price with $$ prince
hotelPrice = 4
percentPrice = (hotelPrice * 100) / 9
print('Percentage of the hotel price with $$ prince')
print(percentPrice)

# ========================================================
