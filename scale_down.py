filename = 'wavelet_yq01-ps-global-42'
output = 'wavelet_yq01-ps-global-42-scaled'
fin = open(filename, 'r')
fout = open(output, 'w')

count = 0
for line in fin:
    count += 1
    if count % 10000 == 0:
        print count
        fout.flush()
    values = line.rstrip().split(',')
    for k in range(2, len(values) - 32):
        if k < 58 + 1:
            values[k] = str(float(values[k]) / 1000)
        else:
            values[k] = str(float(values[k]) / 100000)
    fout.write(','.join(values) + '\n')

fin.close()
fout.close()
