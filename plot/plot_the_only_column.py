import matplotlib.pyplot as plt

data = []
#fin = open('test_power.txt', 'r')
fin = open('all_power', 'r')
for line in fin:
	data.append(float(line))

plt.plot(data)
plt.show()