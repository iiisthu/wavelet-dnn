import random

filename= 'wavelet_yq01-ps-global-42-scaled'
fin= open(filename, 'r')

fout1 = open(filename + '-evaluation', 'w')
fout2 = open(filename + '-train', 'w')
fout3 = open(filename + '-test', 'w')
count_input = 0
count_eval = 0
count_test = 0
count = 0

interval = 200000

for line in fin:
    count += 1
    # evaluation set
    if count >= 500000 and count < 500000 + interval or \
            count >= 1500000 and count < 1500000 + interval or \
            count >= 2500000 and count < 2500000 + interval:
        count_eval += 1
        fout1.write(line.rstrip() + '\n')
    elif random.random() < 0.11 and count_test < 300000:
        count_test += 1  
        fout3.write(line.rstrip() + '\n')
    else:
        fout2.write(line.rstrip() + '\n')
    if count % 100000 ==0:
        print count
        fout1.flush()
        fout2.flush()
        fout3.flush()
fin.close()
fout1.close()
fout2.close()
fout3.close()
