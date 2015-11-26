#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

value=[]
stdev=[]
for i in range(4):
	value.append([])
	stdev.append([])

file=open('l.txt','r')
for i in range(4):
	title=file.readline()
	content=file.readline().split()
	for j in content:
		value[i].append(float(j))
	content=file.readline().split()
	for k in content:
		stdev[i].append(float(k))

x=[i for i in range(200,1200,100)]

#plt.figure(figsize=(18, 6), dpi=100)

plt.rc('xtick', labelsize = 10)
plt.rc('ytick', labelsize = 10)

plt.errorbar(x,value[0],yerr=stdev[0],color='r',label=r"$m-fold$")
plt.errorbar(x,value[1],yerr=stdev[1],color='g',label=r"$Vienna$")

plt.xlabel('Size of RNA',fontsize=15)
plt.ylabel('Time / s',fontsize=15)
#plt.text(55000,0.91,r'$time \ =\ $'+str(time)+r'$\ ps$',color='k',fontsize=18)
plt.grid(True)
plt.xlim(100,1200)
plt.xticks(np.linspace(100,1200,11, endpoint=True))
plt.legend(numpoints=15,prop={'size':18},loc="upper left",frameon=False)
plt.savefig("l-m-v.png")
plt.close()

plt.rc('xtick', labelsize = 10)
plt.rc('ytick', labelsize = 10)

yerr=[]
for i in stdev[2]:
	yerr.append(float(i))

y=value[2]
#plt.plot(x,value[2],'r',label=r"$m-fold$",linewidth=1.5)
#plt.plot(x,value[3],'b',label=r"$Vienna$",linewidth=1.5)
plt.errorbar(x,value[2],yerr=stdev[2],color='r',label=r"$m-fold$")
plt.errorbar(x,value[3],yerr=stdev[3],color='g',label=r"$Vienna$")

plt.xlabel('Size of RNA',fontsize=15)
plt.ylabel('Time / s',fontsize=15)
plt.grid(True)
plt.xlim(100,1200)
plt.xticks(np.linspace(100,1200,11, endpoint=True))
plt.legend(numpoints=15,prop={'size':18},loc="upper left",frameon=False)
plt.savefig("c-m-v.png")
