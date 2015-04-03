from sklearn import preprocessing
import numpy as np

file_name = 'wavelet_yq01-ps-global-42-test'
fin = open(file_name, 'r')
lines = fin.readlines()
fin.close()

data_mat = []
count = 0
for line in lines:
    count += 1
    if count % 10000 == 0:
        print count
    row = []
    values = line.split(',')[1:]
    for k in range(len(values)):
        values[k] = float(values[k])
    data_mat.append(values)

print 'now begin normalizing...'
scaler_file = 'scaler.data'
fin = open(scaler_file, 'r')
lines = fin.readlines()
scaler = preprocessing.StandardScaler(with_mean = True, with_std = True, copy = False)
fin.close()
means = lines[0].split()
stds = lines[1].split()
for k in range(len(means)):
    means[k] = float(means[k])
    stds[k] = float(stds[k])
scaler.mean_ = np.array(means)
scaler.std_ = np.array(stds)

data_mat = np.array(data_mat)
data_mat = scaler.transform(data_mat)

print 'now output~'
output_file = 'dnn-' + file_name
fout = open(output_file, 'a')
length = len(data_mat[0])
print 'length', length
count = 0
for row in data_mat:
    count += 1
    line = '0;0'
    for k in range(1, length):
        line += ' ' + str(row[k])
    line += ';1 ' + str(row[0]) + '\n'
    fout.write(line)
    if count % 10000 == 0:
        print count
        fout.flush()

fout.close()
