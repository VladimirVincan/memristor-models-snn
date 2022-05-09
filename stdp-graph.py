import ltspice
import matplotlib.pyplot as plt
import numpy as np
import os

l = ltspice.Ltspice(os.path.dirname(__file__)+'\\stdp.raw') 
l.parse() 

diff = []
time = []
time_val = 0
time_mid = 0.5

# ---- EDIT ----
time_start = 0.489
time_update = 0.001
# ---- end EDIT ----

print(l.case_count)
for i in range(l.case_count): # Iteration in simulation cases
    V_y = l.get_data('V(y)', i)
    diff.append(-V_y[0] + V_y[-1])
    time.append(time_start + time_val - time_mid)
    time_val += time_update
    print (i)
plt.plot(time, diff, 'bo')
plt.ylabel('Voltage change Δy (V)')
plt.xlabel(r'Inter-pulse interval $t_{gap}$ (s)')
print(diff, time)
plt.show()