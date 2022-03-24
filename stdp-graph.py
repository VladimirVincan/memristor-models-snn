import ltspice
import matplotlib.pyplot as plt
import numpy as np
import os

l = ltspice.Ltspice(os.path.dirname(__file__)+'\\memristor_volRCn.raw') 
l.parse() 

diff = []
time = []
time_val = 0.1
print(l.case_count)
for i in range(l.case_count): # Iteration in simulation cases
    V_y = l.get_data('V(y)', i)
    diff.append(V_y[0] - V_y[-1])
    time.append(time_val)
    time_val += 0.1
    print (i)
print(diff, time)
plt.plot(time, diff)
plt.show()