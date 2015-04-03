import numpy as np

f = open('plot_power', 'r')

mintime=10000000000
maxtime=0
count=0
diff = 0

power=[]

for line in f:
    power.append(int(line))

f.close()        
#print "the range:", mintime, maxtime
#print (maxtime-mintime)/86400
list_1=np.array(power)
#list_2=np.array(power_2)
print np.mean(list_1), np.std(list_1), np.max(list_1), np.min(list_1)
#print np.mean(list_2), np.std(list_2), np.max(list_2), np.min(list_2)
