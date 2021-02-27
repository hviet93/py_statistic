import numpy

miniSystemPrice = [250, 500, 200, 170, 170, 150, 300, 500, 400, 500]
cdQuantities = [3, 1, 3, 5, 3, 3, 3, 5, 3, 1]

# 4

# 4c mean value of the sample
meanPrice = numpy.mean(miniSystemPrice)
print('Mean value of the mini system')
print(meanPrice)  # 314
print('-----------------------------')

# 4c Mean value of CD quantity
meanCD = numpy.mean(cdQuantities)
print('Mean value of CD quantity')
print(meanCD)
print('-----------------------------')
# ========================================================
