import ltspice
import matplotlib.pyplot as plt
import numpy as np
import os
diff = [-0.025849998, -0.025961906, -0.02608341, -0.026228845, -0.026393414, -0.026581973, -0.026789725, -0.027026296, -0.027296454, -0.02759549, -0.027933031, -0.028313845, -0.028733283, -0.02920571, -0.029731244, -0.030764878, -0.03202024, -0.03273973, -0.033536732, -0.034425884, -0.035412103, -0.036505282, -0.037720114, -0.039061666, -0.040554434, -0.042203605, -0.044033885, -0.046055436, -0.048293203, -0.051809072, -0.05452165, -0.05751151, -0.06082374, -0.06447458, -0.06865057, -0.07397923, -0.07884124, -0.08420861, -0.091165215, -0.09762174, -0.10473558, -0.10893819, -0.10893819, -0.10893819, -0.10893819, -0.10893819, -0.10893819, -0.10893819, -0.014424473, 0.0, 0.0, 0.10316676, 0.10316682, 0.10316682, 0.10316688, 0.097317696, 0.08685702, 0.07644713, 0.06770438, 0.05888915, 0.051591814, 0.04496771, 0.038078904, 0.032553315, 0.027540386, 0.022991836, 0.017994523, 0.014210165, 0.010772705, 0.0076525807, 0.0048198104, 0.0022494793, -0.0009242892, -0.0030620098, -0.0050028563, -0.0067673326, -0.008365393, -0.009822935, -0.0111396015, -0.0123414695, -0.013433576, -0.014426202, -0.015329778, -0.016149402, -0.016900837, -0.017578661, -0.018203944, -0.01877132, -0.019286007, -0.019763857, -0.020199448, -0.020968229, -0.021669954, -0.022120774, -0.022429913, -0.022717893, -0.022979379, -0.023219675, -0.023438752, -0.023647249, 
 -0.014424473, -0.060990006, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
 -0.11026803, -0.10072073, -0.091159075, -0.081590116, -0.072014004, -0.0624308, -0.05284041, -0.043242663, -0.03363791, -0.024025947, -0.014407158, -0.024033487, -0.03366679, -0.042871863, -0.050134838, -0.055433482, -0.058764875, -0.060087413, -0.060376942, -0.0606665, -0.060925156,
 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0006981492, 0.0034864545, 0.008368552, 0.015369117, 0.024429083, 0.03472519, 0.04496789, 0.05526185, 0.06553584
 , 0.06553584, 0.06533682, 0.06512737, 0.06442821, 0.061804354, 0.05735731, 0.050988078, 0.042675078, 0.034280002, 0.025877595, 0.017468154
 , 0.017468154, 0.025885403, 0.034310102, 0.04274243, 0.05118227, 0.05962974, 0.068084836, 0.07654756, 0.08501798, 0.093496025, 0.10197538, 0.09567028, 0.089351356, 0.08302683, 0.076696694, 0.07036096, 0.06401962, 0.05767268, 0.051320016, 0.04496169, 0.03859794
 ]
time = [-4.90000000e-01, -4.80000000e-01, -4.70000000e-01, -4.60000000e-01,
 -4.50000000e-01, -4.40000000e-01, -4.30000000e-01, -4.20000000e-01,
 -4.10000000e-01, -4.00000000e-01, -3.90000000e-01, -3.80000000e-01,
 -3.70000000e-01, -3.60000000e-01, -3.50000000e-01, -3.40000000e-01,
 -3.30000000e-01, -3.20000000e-01, -3.10000000e-01, -3.00000000e-01,
 -2.90000000e-01, -2.80000000e-01, -2.70000000e-01, -2.60000000e-01,
 -2.50000000e-01, -2.40000000e-01, -2.30000000e-01, -2.20000000e-01,
 -2.10000000e-01, -2.00000000e-01, -1.90000000e-01, -1.80000000e-01,
 -1.70000000e-01, -1.60000000e-01, -1.50000000e-01, -1.40000000e-01,
 -1.30000000e-01, -1.20000000e-01, -1.10000000e-01, -1.00000000e-01,
 -9.00000000e-02, -8.00000000e-02, -7.00000000e-02, -6.00000000e-02,
 -5.00000000e-02, -4.00000000e-02, -3.00000000e-02, -2.00000000e-02,
 -1.00000000e-02, -1.77635684e-16,  1.00000000e-02,  2.00000000e-02,
  3.00000000e-02,  4.00000000e-02,  5.00000000e-02,  6.00000000e-02,
  7.00000000e-02,  8.00000000e-02,  9.00000000e-02,  1.00000000e-01,
  1.10000000e-01,  1.20000000e-01,  1.30000000e-01,  1.40000000e-01,
  1.50000000e-01,  1.60000000e-01,  1.70000000e-01,  1.80000000e-01,
  1.90000000e-01,  2.00000000e-01,  2.10000000e-01,  2.20000000e-01,
  2.30000000e-01,  2.40000000e-01,  2.50000000e-01,  2.60000000e-01,
  2.70000000e-01,  2.80000000e-01,  2.90000000e-01,  3.00000000e-01,
  3.10000000e-01,  3.20000000e-01,  3.30000000e-01,  3.40000000e-01,
  3.50000000e-01,  3.60000000e-01,  3.70000000e-01,  3.80000000e-01,
  3.90000000e-01,  4.00000000e-01,  4.10000000e-01,  4.20000000e-01,
  4.30000000e-01,  4.40000000e-01,  4.50000000e-01,  4.60000000e-01,
  4.70000000e-01,  4.80000000e-01,  4.90000000e-01,  5.00000000e-01,
  -0.010000000000000009, -0.009000000000000008, -0.008000000000000007, -0.007000000000000006, -0.006000000000000005, -0.0050000000000000044, -0.0040000000000000036, -0.0030000000000000027, -0.0020000000000000018, -0.0010000000000000009, 0.0, 0.0010000000000000009, 0.0020000000000000018, 0.0030000000000000027, 0.0040000000000000036, 0.0050000000000000044, 0.006000000000000005, 0.007000000000000006, 0.008000000000000007, 0.009000000000000008, 0.010000000000000009,
  -0.0010000000000000009, -0.0009000000000000119, -0.0008000000000000229, -0.0006999999999999784, -0.0005999999999999894, -0.0005000000000000004, -0.00040000000000001146, -0.00030000000000002247, -0.00019999999999997797, -9.999999999998899e-05, 0.0, 9.999999999998899e-05, 0.00019999999999997797, 0.00029999999999996696, 0.00039999999999995595, 0.0004999999999999449, 0.0006000000000000449, 0.0007000000000000339, 0.0008000000000000229, 0.0009000000000000119, 0.0010000000000000009,
-0.01100000000000001, -0.01090000000000002, -0.010800000000000032, -0.010699999999999987, -0.010599999999999998, -0.01050000000000001, -0.01040000000000002, -0.010300000000000031, -0.010199999999999987, -0.010099999999999998, -0.010000000000000009, -0.00990000000000002, -0.009800000000000031, -0.009699999999999986, -0.009599999999999997, -0.009500000000000008, -0.00940000000000002, -0.00930000000000003, -0.009199999999999986, -0.009099999999999997, -0.009000000000000008,
  0.0030000000000000027, 0.0030999999999999917, 0.0031999999999999806, 0.0032999999999999696, 0.0033999999999999586, 0.0034999999999999476, 0.0036000000000000476, 0.0037000000000000366, 0.0038000000000000256, 0.0039000000000000146, 0.0040000000000000036, 0.0040999999999999925, 0.0041999999999999815, 0.0042999999999999705, 0.0043999999999999595, 0.0044999999999999485, 0.0046000000000000485, 0.0047000000000000375, 0.0048000000000000265, 0.0049000000000000155, 0.0050000000000000044, 0.005099999999999993, 0.005199999999999982, 0.005299999999999971, 0.00539999999999996, 0.005499999999999949, 0.005600000000000049, 0.005700000000000038, 0.005800000000000027, 0.005900000000000016, 0.006000000000000005, 0.006099999999999994, 0.006199999999999983, 0.006299999999999972, 0.006399999999999961, 0.00649999999999995, 0.00660000000000005, 0.006700000000000039, 0.006800000000000028, 0.006900000000000017, 0.007000000000000006,
  0.009000000000000008, 0.009099999999999997, 0.009199999999999986, 0.009299999999999975, 0.009399999999999964, 0.009499999999999953, 0.009600000000000053, 0.009700000000000042, 0.009800000000000031, 0.00990000000000002, 0.010000000000000009, 0.010099999999999998, 0.010199999999999987, 0.010299999999999976, 0.010399999999999965, 0.010499999999999954, 0.010600000000000054, 0.010700000000000043, 0.010800000000000032, 0.01090000000000002, 0.01100000000000001
  ,0.01100000000000001, 0.011099999999999999, 0.011199999999999988, 0.011299999999999977, 0.011399999999999966, 0.011499999999999955, 0.011600000000000055, 0.011700000000000044, 0.011800000000000033, 0.011900000000000022, 0.01200000000000001
  , 0.01200000000000001, 0.0121, 0.012199999999999989, 0.012299999999999978, 0.012399999999999967, 0.012499999999999956, 0.012600000000000056, 0.012700000000000045, 0.012800000000000034, 0.012900000000000023, 0.013000000000000012, 0.0131, 0.01319999999999999, 0.013299999999999979, 0.013399999999999967, 0.013499999999999956, 0.013600000000000056, 0.013700000000000045, 0.013800000000000034, 0.013900000000000023, 0.014000000000000012
  ]
  
diff_2 = [-0.039416045, -0.039467335, -0.03957081, -0.039691567, -0.03986469, -0.0400728, -0.04033351, -0.040664583, -0.041031003, -0.041485697, -0.04201132, -0.042608052, -0.043311477, -0.04410422, -0.04502198, -0.04604751, -0.047216654, -0.048529953, -0.050023556, -0.051680386, -0.053554684, -0.055647403, -0.057977527, -0.060600013, -0.06349844, -0.067756385, -0.0713214, -0.075276375, -0.07966027, -0.08451256, -0.08989158, -0.09585661, -0.103459984, -0.11067107, -0.11861542, -0.12739414, -0.13811883, -0.1486766, -0.16027308, -0.17393893, -0.18800148, -0.20326638, -0.22096694, -0.23912928, -0.25998837, -0.28153008, -0.28932804, -0.23733455, -0.16756138, 0.0, 0.16116852, 0.26178282, 0.31762868, 0.28783876, 0.26101935, 0.23541027, 0.21264356, 0.19077665, 0.17149854, 0.15292162, 0.1366669, 0.120952845, 0.10726625, 0.09477174, 0.083379686, 0.072090626, 0.06250358, 0.053750455, 0.0457744, 0.03849387, 0.031511843, 0.024891376, 0.019302368, 0.014180958, 0.009508193, 0.005217612, 0.0013126731, -0.0022745132, -0.0055651665, -0.008604616, -0.011367261, -0.0139229, -0.016294122, -0.018455833, -0.021297336, -0.023181856, -0.024926126, -0.026529372, -0.028039247, -0.029431075, -0.030728549, -0.03195551, -0.033111632, -0.034196615, -0.035210133, -0.036176354, -0.037070543, -0.037941456, -0.038764447, -0.039563894
,-0.23733455, -0.14657342, -0.20218006, -0.2028127, -0.07229087, -0.16756138, -0.16153127, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06977022, 0.16116852, 0.06171298, 0.21357161, 0.21461105, 0.14902306, 0.26178282
]
time_2 =  [-0.49, -0.48, -0.47, -0.46, -0.45, -0.44, -0.43, -0.42, -0.41000000000000003, -0.4, -0.39, -0.38, -0.37, -0.36, -0.35, -0.33999999999999997, -0.32999999999999996, -0.31999999999999995, -0.30999999999999994, -0.29999999999999993, -0.2899999999999999, -0.2799999999999999, -0.2699999999999999, -0.2599999999999999, -0.24999999999999994, -0.23999999999999994, -0.22999999999999993, -0.21999999999999992, -0.2099999999999999, -0.1999999999999999, -0.1899999999999999, -0.17999999999999988, -0.16999999999999987, -0.15999999999999986, -0.14999999999999986, -0.13999999999999985, -0.12999999999999984, -0.11999999999999983, -0.10999999999999982, -0.09999999999999981, -0.0899999999999998, -0.0799999999999998, -0.06999999999999978, -0.059999999999999776, -0.04999999999999977, -0.03999999999999976, -0.02999999999999975, -0.01999999999999974, -0.009999999999999731, 2.220446049250313e-16, 0.010000000000000231, 0.02000000000000024, 0.03000000000000025, 0.04000000000000026, 0.050000000000000266, 0.060000000000000275, 0.07000000000000028, 0.0800000000000003, 0.0900000000000003, 0.10000000000000031, 0.11000000000000032, 0.12000000000000033, 0.13000000000000034, 0.14000000000000035, 0.15000000000000036, 0.16000000000000036, 0.17000000000000037, 0.18000000000000038, 0.1900000000000004, 0.2000000000000004, 0.2100000000000004, 0.22000000000000042, 0.23000000000000043, 0.24000000000000044, 0.25000000000000044, 0.26000000000000045, 0.27000000000000046, 0.28000000000000047, 0.2900000000000005, 0.3000000000000005, 0.3100000000000005, 0.3200000000000005, 0.3300000000000005, 0.3400000000000005, 0.35000000000000053, 0.36000000000000054, 0.37000000000000055, 0.38000000000000056, 0.39000000000000057, 0.4000000000000006, 0.4100000000000006, 0.4200000000000006, 0.4300000000000006, 0.4400000000000006, 0.4500000000000006, 0.46000000000000063, 0.47000000000000064, 0.48000000000000065, 0.49000000000000066, 0.5000000000000007
,-0.020000000000000018, -0.018000000000000016, -0.016000000000000014, -0.014000000000000012, -0.01200000000000001, -0.010000000000000009, -0.008000000000000007, -0.006000000000000005, -0.0040000000000000036, -0.0020000000000000018, 0.0, 0.0020000000000000018, 0.0040000000000000036, 0.006000000000000005, 0.008000000000000007, 0.010000000000000009, 0.01200000000000001, 0.014000000000000012, 0.016000000000000014, 0.018000000000000016, 0.020000000000000018
]
#time = np.array(time) - 2
#time = time / 5
#print (time)
diff = np.array(diff)
diff = diff * 1000
diff_2 = np.array(diff_2)
diff_2 = diff_2 * 1000
plt.plot(time, diff, 'bo')
plt.plot(time_2, diff_2, 'ro')
plt.ylabel('Voltage change Δy (mV)')
plt.xlabel(r'time $t_{gap}$ (s)')
print(diff, time)
plt.show()