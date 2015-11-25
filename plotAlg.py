#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt


#Size    500 1000    2000    3000    4000    5000    6000
#Nussinov    0.279042    2.0751384   16.7032976  57.8145788  145.299802  301.487445  519.6531128
#FG 0.0902596   0.6091998   5.5868114   19.6116506  49.3308922  95.646077   162.9072434
#CUDA   0.00875475  0.198791    0.468987    1.194331    2.581748    4.850551    8.273499

size = [500, 1000, 2000, 3000, 4000, 5000, 6000]
nussinov = [0.279042, 2.0751384, 16.7032976, 57.8145788, 145.299802, 301.487445, 519.6531128]
fg = [0.0902596, 0.6091998, 5.5868114, 19.6116506, 49.3308922, 95.646077, 162.9072434]
cuda = [0.00875475, 0.198791, 0.468987, 1.194331, 2.581748, 4.850551, 8.273499]


#plt.figure(figsize=(18, 6), dpi=100)

plt.rc('xtick', labelsize = 10)
plt.rc('ytick', labelsize = 10)

err = 1

plt.errorbar(size,nussinov,yerr=err,marker='x', color='r',label=r"$Nussinov$")
plt.errorbar(size,fg,yerr=err,marker='x', color='g',label=r"$F-G$")
plt.errorbar(size,cuda,yerr=err,marker='x', color='b',label=r"$CUDA$")

plt.xlabel('Size of RNA',fontsize=15)
plt.ylabel('Time (s)',fontsize=15)
#plt.text(55000,0.91,r'$time \ =\ $'+str(time)+r'$\ ps$',color='k',fontsize=18)
plt.grid(True)
plt.xlim(500,6000)
plt.xticks(np.linspace(500,6000,12, endpoint=True))
plt.legend(numpoints=15,prop={'size':18},loc="upper left",frameon=False)
#plt.show()
plt.savefig("algorithmGraph.png")
plt.close()
