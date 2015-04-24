import numpy as np

index = '3'

predict_path = '/home/users/wangguosai/paddle_api_cmd_1_1_0/predict/'
file_name = 'predict-' + index + '.log'
real_data = 'evaluation-data-' + index

fin = open(predict_path + file_name, 'r')
predictions = fin.readlines()
for k in range(len(predictions)):
    predictions[k] = float(predictions[k])
fin.close()
predictions = np.array(predictions)
#print len(predictions)

fin = open(real_data, 'r')
lines = fin.readlines()
fin.close()

# difference and base
mean_value = [5.21315043834e-07, 0.162965178157]
standard_value = [0.00720781506493, 0.0258410281689]

predictions = (predictions * standard_value[0] + mean_value[0]) * 1000

correct, base = [], []
for k in range(len(lines)):
    vals = lines[k].split(',')[0:4]
    correct.append(float(vals[1]))
    base.append(float(vals[3]) * 1000)

correct = np.array(correct)
base = np.array(base)

#print correct
#print base

error = base + predictions - correct
error_rate = error / correct
difference = np.abs(correct - base)
naive_error = difference / correct

print 'mean_difference:', np.mean(difference)
print 'naive error rate', np.mean(naive_error)
print 'max error rate:', np.max(np.abs(error_rate))
print 'mean error rate', np.mean(np.abs(error_rate))
