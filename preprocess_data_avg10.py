import numpy as np
import pywt

# head 1 2 3 4 5 6 tail
def regroup_lines(lines, output_file_name, ws = 8, avg_size = 10):
    length = len(lines)
    
    fout = open(output_file_name, 'w')
    
    wavelet_data = '' 
    for k in range(length - ws - avg_size):
        if k % 10000 == 0:
            print k, 'lines'
            fout.flush()

        head_keys = lines[k].split()[0].split(',')
        head_host, head_timestamp = head_keys[0], int(head_keys[1])
        tail_keys = lines[k + ws + avg_size].split()[0].split(',')
        tail_host, tail_timestamp = tail_keys[0], int(tail_keys[1])
        if head_host != tail_host or head_timestamp + 60 * (ws + avg_size) != tail_timestamp:
            continue
        values = []
        result = [k]
        for i in range(ws + avg_size):
            values.append(lines[k + i].split()[1].split(','))
        # compute average_time
        power_to_predict = []
        for i in range(ws, ws + avg_size):
            power_to_predict.append(float(values[i][0]))
        target_mean = np.mean(power_to_predict)
 
        # add the deviation of power AND THE AABSOLUTE POWER!
        last_power = int(values[ws - 1][0])
        result.append(target_mean)
        result.append(target_mean - last_power)
        result.append(last_power)
        #print result
        for field in range(4, 32):     # There are 28 valid cols in total
            signal = [float(values[i][field]) for i in range(ws)]
            #print signal
            coeffs = pywt.wavedec(signal, 'db1', level=3)
            for i in range(len(coeffs)):
                result += list(coeffs[i])
            

        for i in range(len(result)):
            result[i] = str(result[i])
        #print 'length', len(result)
        wavelet_data = ','.join(result) + '\n'
        fout.write(wavelet_data)
    
    print 'get wavelet_data!'
    
    fout.close()



if __name__=='__main__':
    #file_name = 'yq01-ps-global-42-tail'
    file_name = 'yq01-ps-global-42'
    
    fin = open(file_name, 'r')
    lines = fin.readlines()
    print type(lines)
    fin.close()
    
    output_file_name = 'wavelet_' + file_name
    regroup_lines(lines, output_file_name, ws = 8, avg_size = 10)
