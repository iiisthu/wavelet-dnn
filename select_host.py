import numpy as np

f = open('part-00042', 'r')
fw=open('yq01-ps-global', 'w')

mintime=10000000000
maxtime=0
count=0
diff = 0

power_1=[]
power_2=[]

for line in f:
    count+=1
    if count%1000000==0:
        print count
    p = line.split()
    key = p[0].split(',')
    host=key[0]
    #if host=='yq01-inf-szwg-ch1293-440031.yq01':
    if host.startswith('yq01-ps-global-'):
        fw.write(line.rstrip() + '\n')
f.close()
fw.close()
