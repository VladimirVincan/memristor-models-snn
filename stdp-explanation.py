import ltspice
import matplotlib.pyplot as plt
import numpy as np
import os

l = ltspice.Ltspice(os.path.join(os.path.dirname(__file__), 'stdp.raw'))
l.parse()

time = l.get_time()
print(l.case_count)
print(l.variables)
fig, axs = plt.subplots(3)
vs = l.get_data('V(Vm)', 0)
vmid = l.get_data('V(Vmid)', 0)
vy = l.get_data('V(y)', 0)
axs[0].plot(time, vs-vmid)
axs[1].plot(time, vmid)
axs[2].plot(time, vy)
axs[0].set_ylabel('Presynaptic pulse', fontweight='bold')
axs[1].set_ylabel('Postsynaptic pulse', fontweight='bold')
axs[2].set_ylabel('Voltage change Δy [mV]', fontweight='bold')
fig.align_ylabels(axs[:])
fig.align_ylabels(axs[:])
fig.autofmt_ydate()
fig.tight_layout()
plt.show()
