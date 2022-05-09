import ltspice
import matplotlib.pyplot as plt
import numpy as np
import os

l = ltspice.Ltspice(os.path.join(os.path.dirname(__file__), '4s2n.raw'))
l.parse()

fig, axs = plt.subplots(3)

time = l.get_time()*1000
vs0 = l.get_data('V(vs0)')
vs1 = l.get_data('V(vs1)')
vn0 = l.get_data('V(vn0)')
vn1 = l.get_data('V(vn1)')

in0 = l.get_data('I(R1)')
in1 = l.get_data('I(R2)')
ic0 = l.get_data('I(C1)')
ic1 = l.get_data('I(C2)')

axs[0].plot(time, vs0, '-', label='v(v0)', linewidth=2.2)
axs[0].plot(time, vs1, '--', label='v(v1)', linewidth=2.2)
axs[0].plot(time, vn0, '-.', label='v(n0)', linewidth=2.2)
axs[0].plot(time, vn1, ':', label='v(n1)', linewidth=2.2)

axs[1].plot(time, vs0-vn0, '-', label='v(s00)', linewidth=2.2)
axs[1].plot(time, vs0-vn1, '--', label='v(s01)', linewidth=2.2)
axs[1].plot(time, vs1-vn0, '-.', label='v(s10)', linewidth=2.2)
axs[1].plot(time, vs1-vn1, ':', label='v(s11)', linewidth=2.2)

axs[2].plot(time, in0, '-', label='i(n0)', linewidth=2.2)
axs[2].plot(time, ic0, '--', label='i(c0)', linewidth=2.2)
axs[2].plot(time, in1, '-.', label='i(n1)', linewidth=2.2)
axs[2].plot(time, ic1, ':', label='i(c1)', linewidth=2.2)

axs[0].set_xlim((0, 31))
axs[1].set_xlim((0, 31))
axs[2].set_xlim((0, 31))
axs[0].set_ylabel('voltage [V]', fontweight='bold')
axs[1].set_ylabel('voltage [V]', fontweight='bold')
axs[2].set_ylabel('current [A]', fontweight='bold')
plt.xlabel("time [ms]", fontweight='bold')
axs[0].legend(bbox_to_anchor=(0.5, 1.2), loc="center", ncol=4)
axs[1].legend(bbox_to_anchor=(0.5, 1.2), loc="center", ncol=4)
axs[2].legend(bbox_to_anchor=(0.5, 1.2), loc="center", ncol=4)
fig.align_ylabels(axs[:])
fig.tight_layout()
plt.savefig('fig5', dpi=300)
plt.show()
