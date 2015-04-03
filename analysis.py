import numpy as np

f = open('part-00042', 'r')

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
    if host.startswith('yq01-inf-szwg'):
    #if host.startswith('yq01-ps-global-'):
        #timestamp=int(key[1])
        #print int(timestamp)
        #if timestamp>maxtime:
        #    maxtime=timestamp
        #if timestamp<mintime:
        #    mintime=timestamp
        value=p[1].split(',')
        power_1.append(int(value[0]))
#    elif host.startswith('yq01-sys-hsc08-m12'):
#        value=p[1].split(',')
#        power_2.append(int(value[0]))


f.close()        
#print "the range:", mintime, maxtime
#print (maxtime-mintime)/86400
#list_1=np.array(power_1)
#list_2=np.array(power_2)
print np.mean(list_1), np.std(list_1), np.max(list_1), np.min(list_1)
#print np.mean(list_2), np.std(list_2), np.max(list_2), np.min(list_2)

f=open('plot_power', 'w')
for k in power_1:
    f.write(str(k) + '\n')
f.close()
