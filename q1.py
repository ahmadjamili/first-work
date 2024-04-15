import numpy as np
def moving_average(data_list,window_size):
    
    window_averages=[]
    window_sum=0
    z=0
    for i in range(len(data_list)):
        window_sum+=data_list[i]
        z+=1
        if i>=window_size:
            
            window_sum-=(data_list[i-window_size])
        if z>=window_size:
            window_averages.append(window_sum/window_size)
            
        
    return np.array(window_averages)
    
    
