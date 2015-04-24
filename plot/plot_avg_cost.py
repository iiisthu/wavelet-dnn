import matplotlib.pyplot as plt

training_cost, test_cost = [], []
fin = open('paddle_trainer.INFO', 'r')
for line in fin.readlines():
    values = line.split()
    if len(values) == 9:
        cost = float(values[7].split('=')[1])
        training_cost.append(cost)
fin.close()

fin = open('tester.log', 'r')
for line in fin.readlines():
    values = line.split()
    if len(values) == 8 and values[3].startswith('Trainer'):
        cost = float(values[6].split('=')[1])
        test_cost.append(cost)
fin.close()

plt.plot(training_cost)
plt.plot(test_cost)
plt.show()