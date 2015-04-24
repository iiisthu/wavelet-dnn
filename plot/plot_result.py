import matplotlib.pyplot as plt
import numpy as np
import math

fin = open('result.txt', 'r')
lines = fin.readlines()
data = []
for line in lines:
    v = line.split()
    for k in range(len(v)):
        v[k] = float(v[k])
    data.append(v)

length = len(data)

real = [data[k][0] for k in range(length)]
pre = [data[k][1] for k in range(length)]
sq_error = [data[k][2] for k in range(length)]
error = [math.sqrt(data[k][2]) for k in range(length)]

correct_count = 0.0
for k in range(length):
    if real[k] * pre[k] > 0:
        correct_count += 1.0
print 'right direction', correct_count / length
print 'square error rate', np.mean(sq_error)
print 'mean error rate', np.mean(error)

plt.plot(real)
plt.plot(pre)
plt.show()